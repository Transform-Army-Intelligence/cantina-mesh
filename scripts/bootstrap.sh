#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

log() {
  printf '[cantina-bootstrap] %s\n' "$1"
}

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  fi
}

pick_python() {
  if command -v python3 >/dev/null 2>&1; then
    printf 'python3'
    return
  fi

  if command -v python >/dev/null 2>&1; then
    printf 'python'
    return
  fi

  printf 'Python interpreter not found. Install Python 3.9+ and retry.\n' >&2
  exit 1
}

main() {
  local python_cmd

  require_command bash
  python_cmd="$(pick_python)"

  log "Using interpreter: ${python_cmd}"
  log "Creating virtual environment at ${VENV_DIR}"
  "${python_cmd}" -m venv "${VENV_DIR}"

  # shellcheck source=/dev/null
  source "${VENV_DIR}/bin/activate"

  log "Upgrading packaging tools"
  python -m pip install --upgrade pip setuptools wheel

  log "Installing protobuf and gRPC tooling"
  python -m pip install grpcio protobuf grpcio-tools

  log "Generating Python protobuf bindings"
  python -m grpc_tools.protoc -I "${ROOT_DIR}/proto" --python_out="${ROOT_DIR}/sdk/python" --grpc_python_out="${ROOT_DIR}/sdk/python" "${ROOT_DIR}/proto/cantina.proto"

  log "Installing tai-cantina SDK in editable mode"
  python -m pip install -e "${ROOT_DIR}/sdk/python"

  log "Bootstrap complete"
  printf '\n'
  printf 'Activate the environment with:\n'
  printf '  source %s/bin/activate\n' "${VENV_DIR}"
  printf '\n'
  printf 'Smoke test:\n'
  printf '  python -c "from tai_cantina import CantinaClient; print(CantinaClient())"\n'
}

main "$@"
