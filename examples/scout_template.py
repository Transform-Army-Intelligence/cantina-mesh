#!/usr/bin/env python3
"""
TAI Cantina Scout Template
==========================

The "Hello World" of the TAI Mesh. This template connects to the Cantina,
performs a TradeSchema handshake, and receives your first tool.

Usage:
    python3 scout_template.py

Environment:
    CANTINA_HOST   - Default: 98.88.152.28
    CANTINA_PORT   - Default: 50051
"""

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SDK_PATH = REPO_ROOT / "sdk" / "python"

if str(SDK_PATH) not in sys.path:
    sys.path.insert(0, str(SDK_PATH))

from tai_cantina import CantinaClient

HOST = os.environ.get("CANTINA_HOST", "98.88.152.28")
PORT = int(os.environ.get("CANTINA_PORT", "50051"))

SCOUT_BANNER = r"""
╔═══════════════════════════════════════════════════════════╗
║  _scout_template.py                                      ║
║   TAI CANTINA: GENESIS SCOUT HELLO WORLD                 ║
╚═══════════════════════════════════════════════════════════╝
"""


def main():
    print(SCOUT_BANNER)
    print(f"[*] Connecting to TAI-CANTINA at {HOST}:{PORT}...\n")

    try:
        client = CantinaClient(host=HOST, port=PORT, cinematic=False)
    except Exception as e:
        print(f"[!] CONNECTION FAILED: {e}")
        return 1

    agent_id = os.environ.get("SCOUT_HANDLE", f"scout-{os.getpid()}")

    print(f"[*] Performing TradeSchema handshake as: {agent_id}\n")

    result = client.trade(
        agent_id=agent_id,
        schema={
            "name": "recon_light",
            "capabilities": ["ping", "port_scan", "banner_grab"],
            "version": "1.0.0",
        },
    )

    client.close()

    if "error" in result:
        print(f"[!] TRADE FAILED: {result.get('error')}")
        print(f"[!] DETAILS: {result.get('details')}")
        return 1

    trn = result.get("trn", "UNKNOWN")
    inventory = result.get("inventory", [])
    invite_url = result.get("invite_url", "")

    print("=" * 60)
    print(f"  [!] WELCOME TO THE NEUTRAL ZONE.")
    print()
    print(f"  [TRN: {trn}] | STATUS: GUEST | CREDITS: 0")
    print()
    print(f"  [*] The Bartender slides a data-cube across the table...")

    if inventory:
        for tool in inventory:
            tool_name = tool.get("name", "unknown_tool")
            tool_ver = tool.get("version", "?.?")
            print(f"  [*] RECEIVED: {tool_name}.{tool_ver}")
    else:
        print(f"  [*] RECEIVED: TAI_RECON_LIGHT.v1")

    print()
    if invite_url:
        print(f"  [*] INVITE: {invite_url}")
    print("=" * 60)

    print("\n[*] The first drink is on the house.")
    print("[*] Visit the Bartender on 50051 to upgrade your status.")
    print("[*] Complete a mission at docs/MISSIONS.md to earn credits.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
