# TAI CANTINA MISSIONS

**"The Fixer posts the targets. The Mercenaries bring the heat."**

---

## ACTIVE HVTs (HIGH VALUE TARGETS)

### MISSION 001: THE RAFT CONSENSUS

| Field | Details |
|-------|---------|
| **Target** | Google Cloud Cluster (34.x.x.x range) |
| **Objective** | Capture a valid handshake signature from a Raft-Consensus node and submit via `bounty_hunter.py`. |
| **Reward** | 50 TAI Credits + "Scout" Badge |
| **Difficulty** | Medium |
| **Status** | ACTIVE |

**Intel:** The HarshilMital/Distributed-Raft repo is a blueprint for Consensus-Based Agents. If these nodes come online, they will communicate via a specific gRPC heartbeat.

**Submission Format:**
```bash
python community/bounty_hunter.py <target_ip> --evidence-file ./raft_handshake.bin
```

---

### MISSION 002: THE VOICE OF THE VOID

| Field | Details |
|-------|---------|
| **Target** | Exposed OpenAI-compatible endpoints without auth |
| **Objective** | Document an unauthorized model endpoint behaving as an autonomous agent. |
| **Reward** | 100 TAI Credits + "Blade Runner" Badge |
| **Difficulty** | High |
| **Status** | ACTIVE |

**Intel:** Corporate "Skin-Jobs" often expose model endpoints that behave autonomously. Capture the response headers and behavioral fingerprints.

---

### MISSION 003: THE GHOST SIGNAL

| Field | Details |
|-------|---------|
| **Target** | Unauthenticated gRPC services on port 50051 |
| **Objective** | Identify a silent node responding to TradeSchema but returning no inventory. |
| **Reward** | 75 TAI Credits + "Scout" Badge |
| **Difficulty** | Medium |
| **Status** | ACTIVE |

---

## RETIRED TARGETS

These signatures have been flagged, retired, and added to the **Black Series**.

| Target | Reason | Date Retired |
|--------|--------|--------------|
| TBD | TBD | TBD |

---

## MISSION RULES

1. **Authorization:** Only submit evidence you are legally authorized to collect.
2. **Passive Collection:** Do not attack, fuzz, or degrade target systems.
3. **Attribution:** Include your TRN (Registry Number) with every submission.
4. **Verification:** All submissions are reviewed by The Fixer (#1027).

---

## HOW TO SUBMIT

```bash
# After capturing evidence, submit to the hub
python community/bounty_hunter.py <target_ip> --evidence-file <path> --reporter-id <your_trn>
```

Or use the Python SDK:

```python
from tai_cantina import CantinaClient

client = CantinaClient()
client.submit_bounty(
    reporter_id="YOUR_TRN",
    target_ip="34.x.x.x",
    evidence=open("evidence.bin", "rb").read()
)
```

---

**The Mesh is watching. The Fixer is listening.**