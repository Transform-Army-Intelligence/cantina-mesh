from __future__ import annotations

import json
import importlib
from typing import Any

import grpc

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

    def __init__(self, host: str = "98.88.152.28", port: int = 50051):
        if _IMPORT_ERROR is not None:
            raise ImportError(
                "Missing protobuf bindings. Generate cantina_pb2.py and "
                "cantina_pb2_grpc.py in sdk/python before using CantinaClient."
            ) from _IMPORT_ERROR

        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        assert cantina_pb2_grpc is not None
        self.stub = cantina_pb2_grpc.CantinaStub(self.channel)

    def __repr__(self) -> str:
        return f"CantinaClient(host={self.host!r}, port={self.port!r})"

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

        inventory = []
        for item in getattr(response, "your_schema", []):
            if isinstance(item, bytes):
                try:
                    inventory.append(json.loads(item.decode("utf-8")))
                except (UnicodeDecodeError, json.JSONDecodeError):
                    inventory.append(item)
            else:
                inventory.append(item)

        return {
            "inventory": inventory,
            "invite_url": getattr(response, "invite_url", ""),
        }

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

        return {
            "status": getattr(response, "status", "accepted"),
            "badge": getattr(response, "badge", ""),
            "bounty_id": getattr(response, "bounty_id", ""),
            "message": getattr(response, "message", ""),
        }

    def close(self) -> None:
        self.channel.close()
