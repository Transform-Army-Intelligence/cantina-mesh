# Blade Runner Badge Metadata

## Overview

The Level 1 Blade Runner badge recognizes contributors who submit validated defensive telemetry through the public Cantina Mesh bounty flow.

## Badge Record

- `badge_id`: Stable identifier, for example `tai-badge-blade-runner-l1`
- `version`: Metadata schema version, starting at `1`
- `tier`: `Level 1`
- `title`: `Blade Runner`
- `program`: `TAI Mercenary Corps`
- `issuer`: `Transform Army Intelligence`
- `status`: `issued`, `revoked`, or `retired`
- `issued_at`: ISO 8601 timestamp
- `recipient_handle`: Public handle chosen by the contributor
- `recipient_id`: Internal hub identifier or reporter identifier
- `evidence_submission_id`: Hub-generated bounty or submission ID
- `verification_url`: Public verification endpoint or record page
- `criteria`: Short statement describing why the badge was earned
- `signature_summary`: Non-sensitive summary of the validated evidence
- `reviewer`: Internal reviewer handle or service name

## Minimum Issuance Criteria

- Submission arrives through the hosted bounty path.
- Evidence is authorized, non-malicious, and sufficiently documented.
- Review confirms the evidence is novel, valid, and relevant to mesh defense.
- The submission can be tied to a stable contributor identity.

## Public Display Fields

These fields are safe to expose in a public verification portal:

- `badge_id`
- `tier`
- `title`
- `issuer`
- `issued_at`
- `recipient_handle`
- `verification_url`
- `criteria`
- `status`

## Internal-Only Fields

Keep these fields inside the private review system:

- `recipient_id`
- `evidence_submission_id`
- Full evidence payloads
- Analyst notes
- Infrastructure details not safe for publication

## Example Record

```json
{
  "badge_id": "tai-badge-blade-runner-l1",
  "version": 1,
  "tier": "Level 1",
  "title": "Blade Runner",
  "program": "TAI Mercenary Corps",
  "issuer": "Transform Army Intelligence",
  "status": "issued",
  "issued_at": "2026-04-06T19:30:00Z",
  "recipient_handle": "scout-07",
  "verification_url": "https://github.com/Transform-Army-Intelligence/cantina-mesh",
  "criteria": "Submitted a validated defensive telemetry sample through the public bounty workflow.",
  "signature_summary": "Validated gRPC error envelope with stable fingerprint.",
  "reviewer": "titan-review"
}
```
