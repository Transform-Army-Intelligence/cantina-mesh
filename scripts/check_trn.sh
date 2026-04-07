#!/usr/bin/env bash

set -euo pipefail

HOST="${CANTINA_HOST:-98.88.152.28}"
PORT="${CANTINA_PORT:-50051}"

echo "=========================================="
echo "  TAI CANTINA: IDENTITY CHECK"
echo "=========================================="
echo ""
echo "[*] Connecting to TAI-CANTINA at ${HOST}:${PORT}..."
echo ""

TRN_RESPONSE=$(echo "PING" | nc -w 3 "${HOST}" "${PORT}" 2>/dev/null || echo "")

if [[ -z "${TRN_RESPONSE}" ]]; then
    echo "[!] CANTINA IS SILENT."
    echo "[!] Either the node is down or you're on the wrong frequency."
    echo "[*] Try: Trade Frequency (50051)"
    exit 1
fi

TRN_NUMBER=$(echo "${TRN_RESPONSE}" | grep -oP 'TRN:\s*#\K[0-9]+' || echo "UNKNOWN")
STATUS=$(echo "${TRN_RESPONSE}" | grep -oP 'STATUS:\s*\K[A-Z]+' || echo "UNKNOWN")

echo "[!] WELCOME TO THE NEUTRAL ZONE."
echo ""
echo "  [TRN: #${TRN_NUMBER}] | STATUS: ${STATUS} | CREDITS: 0"
echo ""
echo "[*] The Doorman nods silently."
echo "[*] Visit the Bartender on 50051 to claim your first drink."

exit 0