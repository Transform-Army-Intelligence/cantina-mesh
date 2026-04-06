# Final Deployment Orders

## 1. First Release

Use the contents of `docs/launch_signal.md` as the body for the first GitHub Release and tag it as `v1.0.0-Sovereign`.

## 2. Internal Seed List

Keep suspected infrastructure targets and unverified IP observations in a private `WATCH_LIST.md` inside the private vault. Do not publish raw target lists in the public repository or public discussions until they are validated and safe to disclose.

## 3. First Badge Issuance

After the first legitimate bounty submission reaches the hosted hub and passes review, generate and issue the first Blade Runner badge for that contributor.

## 4. Public Release Checklist

- Confirm `scripts/bootstrap.sh` generates protobuf bindings successfully.
- Confirm `sdk/python/tai_cantina.py` imports after bootstrap.
- Confirm `community/bounty_hunter.py` submits evidence without active probing features.
- Confirm `docs/launch_signal.md` is ready for release-note reuse.
- Confirm MIT licensing and repository hygiene files are present.
