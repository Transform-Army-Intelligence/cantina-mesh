# Blade Runner Verification Flow

## Objective

Issue Level 1 Blade Runner badges for validated, defensively collected submissions without exposing sensitive telemetry or internal infrastructure details.

## Flow

1. Contributor submits evidence through `community/bounty_hunter.py` or a future portal.
2. Hosted hub records a submission ID, timestamp, reporter identifier, and evidence metadata.
3. Internal review checks authorization, integrity, relevance, and novelty.
4. Approved submissions receive a normalized signature summary and badge decision.
5. Issued badges are published through a lightweight verification record using the public-safe metadata set.

## Validation Checks

- **Authorization:** Evidence must be collected lawfully and within the contributor's authority.
- **Integrity:** Submission must be intact, readable, and attributable to a specific event.
- **Novelty:** Evidence should add new defensive value or strengthen an existing signature with higher confidence.
- **Relevance:** Evidence should relate to exposed coordination, agent exchange, or mesh-adjacent defensive telemetry.

## Decision Outcomes

- `issued`: Submission passes review and earns a badge.
- `needs_more_context`: Submission is promising but lacks sufficient metadata.
- `rejected`: Submission is invalid, unauthorized, or out of scope.
- `revoked`: Previously issued badge is withdrawn due to later evidence or policy review.

## Verification Portal Requirements

- Show badge title, tier, issuer, recipient handle, issue date, and current status.
- Show a short criteria statement and non-sensitive signature summary.
- Avoid publishing raw IPs, packet captures, secrets, or internal notes.
- Support revocation status so public trust can be maintained over time.

## Issuance Checklist

- Confirm submission ID is present.
- Confirm reviewer approved the submission.
- Generate the metadata record using `docs/blade_runner_badge_metadata.md`.
- Publish the public-safe record.
- Notify the recipient with the badge identifier and verification URL.

## Operational Notes

- Badge issuance should remain a defensive recognition workflow, not a bounty-for-access program.
- Public metadata should reward contributions without disclosing protected intelligence.
- Internal review artifacts should remain in the private vault, not in this public repository.
