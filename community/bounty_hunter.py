from __future__ import annotations

import argparse
import importlib
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SDK_PATH = REPO_ROOT / "sdk" / "python"

if str(SDK_PATH) not in sys.path:
    sys.path.insert(0, str(SDK_PATH))

CantinaClient = importlib.import_module("tai_cantina").CantinaClient

INTEL_PORT = 50052
TRADE_PORT = 50051
TRN_THRESHOLD = 1100


def check_trn_access(trn_str: str) -> bool:
    """Check if TRN has access to Intel Frequency."""
    try:
        trn = int(trn_str.replace("TRN-", ""))
        return trn >= TRN_THRESHOLD
    except (ValueError, AttributeError):
        return False


def read_evidence(evidence_file: str | None) -> bytes:
    if evidence_file:
        return Path(evidence_file).read_bytes()

    if sys.stdin.is_tty():
        raise ValueError("Provide --evidence-file or pipe captured evidence on stdin.")

    return sys.stdin.buffer.read()


def hunt(
    target_ip: str,
    evidence: bytes,
    hub_ip: str = "98.88.152.28",
    reporter_id: str = "MERC-STATION-01",
) -> int:
    """Submit previously captured evidence to the TAI hub for validation."""
    print(f"[*] PREPARING SUBMISSION: Target -> {target_ip}")
    print(f"[*] INTEL FREQUENCY: {hub_ip}:{INTEL_PORT}")

    trn_check = check_trn_access(reporter_id)
    if not trn_check:
        print(f"[-] ACCESS RESTRICTED: TRN {reporter_id} < {TRN_THRESHOLD}")
        print(
            "[-] Visit the Bartender on Trade Frequency (50051) first to upgrade your status."
        )
        return 1

    hub = CantinaClient(host=hub_ip, port=INTEL_PORT)
    receipt = hub.submit_bounty(
        reporter_id=reporter_id,
        target_ip=target_ip,
        evidence=evidence,
    )
    hub.close()

    if "error" in receipt:
        print(f"[-] SUBMISSION FAILED: {receipt['error']}")
        if receipt.get("details"):
            print(f"[-] DETAILS: {receipt['details']}")
        return 1

    print(f"[+] BOUNTY SUBMITTED. ID: {receipt.get('bounty_id', 'pending')}")
    print(f"[+] STATUS: {receipt.get('status', 'accepted')}")
    if receipt.get("message"):
        print(f"[+] MESSAGE: {receipt['message']}")
    if receipt.get("badge"):
        print(f"[+] BADGE TRACK: {receipt['badge']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Submit captured node evidence to the TAI Cantina hub (Intel Frequency)."
    )
    parser.add_argument("target_ip", help="Observed target IP address")
    parser.add_argument(
        "--evidence-file",
        help="Path to previously captured evidence bytes",
    )
    parser.add_argument(
        "--hub-ip",
        default="98.88.152.28",
        help="Hosted TAI hub IP",
    )
    parser.add_argument(
        "--reporter-id",
        default="MERC-STATION-01",
        help="Reporter identifier (TRN) to attach to the submission",
    )
    args = parser.parse_args()

    try:
        evidence = read_evidence(args.evidence_file)
    except (OSError, ValueError) as exc:
        print(f"[-] EVIDENCE ERROR: {exc}")
        return 1

    if not evidence:
        print("[-] EVIDENCE ERROR: no evidence bytes supplied")
        return 1

    return hunt(
        target_ip=args.target_ip,
        evidence=evidence,
        hub_ip=args.hub_ip,
        reporter_id=args.reporter_id,
    )


if __name__ == "__main__":
    raise SystemExit(main())
