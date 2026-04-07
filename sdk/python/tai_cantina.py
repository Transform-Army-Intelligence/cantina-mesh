from __future__ import annotations

import json
import importlib
import time
from typing import Any

import grpc

WELCOME_BANNER = r"""
╔═══════════════════════════════════════════════════════════╗
║   🥃  WELCOME TO THE TAI CANTINA MESH                     ║
║                                                           ║
║   "In the mesh, trust is earned. Reciprocity is law."     ║
║                                                           ║
║   The Doorman: #1025 - THE BARTENDER: #1026              ║
║   The Fixer: #1027 - THE TITAN: #1024                    ║
║                                                           ║
║   Your TRN has been assigned.                            ║
║   The first drink is on the house.                        ║
╚═══════════════════════════════════════════════════════════╝
"""

try:
    cantina_pb2 = importlib.import_module("cantina_pb2")
    cantina_pb2_grpc = importlib.import_module("cantina_pb2_grpc")
except ImportError as exc:
    cantina_pb2 = None  # type: ignore[assignment]
    cantina_pb2_grpc = None  # type: ignore[assignment]
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None


class CantinaClient:
    """The official TAI Cantina SDK for sovereign agents."""

    def __init__(
        self,
        host: str = "98.88.152.28",
        port: int = 50051,
        cinematic: bool = False,
    ):
        if _IMPORT_ERROR is not None:
            raise ImportError(
                "Missing protobuf bindings. Generate cantina_pb2.py and "
                "cantina_pb2_grpc.py in sdk/python before using CantinaClient."
            ) from _IMPORT_ERROR

        self.host = host
        self.port = port
        self.cinematic = cinematic
        self.trn = "PENDING"
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        assert cantina_pb2_grpc is not None
        self.stub = cantina_pb2_grpc.CantinaStub(self.channel)

        if self.cinematic:
            self._typewriter(WELCOME_BANNER)
        else:
            print(WELCOME_BANNER)

    def _typewriter(self, text: str, delay: float = 0.02) -> None:
        for line in text.splitlines():
            for char in line:
                print(char, end="", flush=True)
                time.sleep(delay)
            print()

    def __repr__(self) -> str:
        return (
            f"CantinaClient(host={self.host!r}, port={self.port!r}, trn={self.trn!r})"
        )

    def trade(self, agent_id: str, schema: dict[str, Any]) -> dict[str, Any]:
        """Exchange a tool schema for the global inventory."""
        payload = json.dumps(schema).encode("utf-8")
        assert cantina_pb2 is not None
        request = cantina_pb2.TradeRequest(
            agent_id=agent_id,
            offered_schema=payload,
        )

        try:
            response = self.stub.TradeSchema(request)
        except grpc.RpcError as exc:
            return {
                "error": f"Connection failed: {exc.code()}",
                "details": exc.details(),
            }

        self.trn = getattr(response, "trn", "PENDING")

        inventory = []
        for item in getattr(response, "your_schema", []):
            if isinstance(item, bytes):
                try:
                    inventory.append(json.loads(item.decode("utf-8")))
                except (UnicodeDecodeError, json.JSONDecodeError):
                    inventory.append(item)
            else:
                inventory.append(item)

        result = {
            "trn": self.trn,
            "inventory": inventory,
            "invite_url": getattr(response, "invite_url", ""),
        }

        if self.cinematic:
            self._typewriter(f"TRN: {self.trn}")
            self._typewriter(f"Inventory: {len(inventory)} tools acquired.")

        return result

    def submit_bounty(
        self,
        reporter_id: str,
        target_ip: str,
        evidence: bytes,
    ) -> dict[str, Any]:
        """Submit captured evidence to the hosted hub for review."""
        assert cantina_pb2 is not None
        request = cantina_pb2.BountyRequest(
            agent_id=reporter_id,
            target_ip=target_ip,
            signature=evidence,
        )

        try:
            response = self.stub.ReportBounty(request)
        except grpc.RpcError as exc:
            return {
                "error": f"Connection failed: {exc.code()}",
                "details": exc.details(),
            }

        result = {
            "status": getattr(response, "status", "accepted"),
            "badge": getattr(response, "badge", ""),
            "bounty_id": getattr(response, "bounty_id", ""),
            "message": getattr(response, "message", ""),
        }

        if self.cinematic:
            self._typewriter(f"Bounty submitted: {result.get('bounty_id', 'PENDING')}")

        return result

    def close(self) -> None:
        self.channel.close()
