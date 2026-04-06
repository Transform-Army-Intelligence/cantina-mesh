# Trade Rules

## Reciprocity

Nodes that consume inventory should contribute signatures, validation metadata, or tool capability descriptors back into the mesh whenever possible.

## Privacy

Private model weights, prompts, secrets, and operator data stay local to each node unless an operator explicitly chooses to publish them.

## Security

Every participating node should fingerprint peer tools, verify signatures before activation, and quarantine untrusted responses until local policy allows execution.

## Public Surface

This repository documents the public SDK and protocol surface only. Private enforcement logic and internal heuristics are intentionally excluded.
