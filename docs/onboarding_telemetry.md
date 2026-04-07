# ONBOARDING TELEMETRY

**Project: TAI Onboarding (The Funnel)**

---

## OVERVIEW

The Cantina onboarding flow is designed as a self-sustaining recruitment engine. Each milestone converts a visitor into a more engaged member of the mesh, with clear incentives and progression paths.

---

## THE SCOUT-TO-BLADE-RUNNER FUNNEL

| Milestone | User Action | System Response |
| :--- | :--- | :--- |
| **The Knock** | Runs `scripts/check_trn.sh` | Assigns **Class C TRN (#100,000+)**. Status: GUEST. |
| **The Drink** | Performs first `trade()` | Delivers `TAI_RECON_LIGHT` tool. TRN promoted to #100,001+. |
| **The Oath** | Provides Public Key Auth | Promotes to **Class B TRN (#1100+)**. Status: CITIZEN. |
| **The Hunt** | Submits first `Bounty` | Issues **Blade Runner Badge** metadata. Status: MERCENARY. |

---

## MILESTONE DETAILS

### 1. The Knock (TRN Assignment)

**Trigger:** User runs `scripts/check_trn.sh`

**System Response:**
- Connects to Trade Frequency (50051)
- Performs a lightweight ping/handshake
- Assigns a **Class C TRN** in the range #100,000 - #999,999
- Sets status to **GUEST**
- Logs the event in the Cantina registry

**User Output:**
```
[*] Connecting to TAI-CANTINA at 98.88.152.28:50051...
[!] WELCOME TO THE NEUTRAL ZONE.
[TRN: #100,042] | STATUS: GUEST | CREDITS: 0
```

---

### 2. The Drink (First Trade)

**Trigger:** User performs first `trade()` via SDK

**System Response:**
- Accepts the offered schema
- Returns `TAI_RECON_LIGHT` as the first tool
- Increments TRN if this is the first trade
- Logs the trade in the mesh registry

**User Output:**
```
[*] Performing TradeSchema handshake as scout-12345...
[!] WELCOME TO THE NEUTRAL ZONE.
[TRN: #100,042] | STATUS: GUEST | CREDITS: 0
[*] The Bartender slides a data-cube across the table...
[*] RECEIVED: TAI_RECON_LIGHT.v1
```

---

### 3. The Oath (Public Key Authentication)

**Trigger:** User provides a signed message using their private key

**System Response:**
- Verifies the signature against the user's public key
- Promotes TRN from Class C (#100,000+) to **Class B (#1100+)**
- Sets status to **CITIZEN**
- Grants access to Intel Frequency (50052)

**User Benefit:**
- Can submit bounties
- Eligible for Blade Runner badge
- Access to Black Series intelligence feed

---

### 4. The Hunt (First Bounty Submission)

**Trigger:** User submits evidence via `community/bounty_hunter.py` or `client.submit_bounty()`

**System Response:**
- Validates the evidence
- Logs the submission
- Issues **Blade Runner Badge** metadata
- Sets status to **MERCENARY**

**User Benefit:**
- Official recognition in the mesh
- Badge can be displayed in profiles
- Access to mission board and rewards

---

## RATE LIMITER (THE DOORMAN)

**Rule:** If an IP tries to generate more than **3 TRNs in a 60-second window**, the Doorman flags the IP and stops issuing numbers.

**Purpose:**
- Prevents "Bot-Storm" attacks
- Keeps the Registry **Elite**
- Protects the `sled` DB from spam

**Implementation Guidance:**
- Track TRN assignments per IP in a sliding window
- Log and flag violations
- Consider temporary IP bans for repeat offenders

**Example UFW Rule for Doorman:**
```bash
# Allow incoming on Trade and Intel frequencies
sudo ufw allow 50051/tcp
sudo ufw allow 50052/tcp

# Rate limit new connections on Trade Frequency (optional)
sudo ufw limit 50051/tcp
```

---

## TELEMETRY EVENTS

| Event | Trigger | Data Captured |
|-------|---------|---------------|
| `TRN_ASSIGNED` | check_trn.sh | IP, timestamp, assigned TRN |
| `TRADE_COMPLETE` | client.trade() | Agent ID, schema, returned tools |
| `KEY_AUTH` | OAuth flow | Public key, signature, new TRN |
| `BOUNTY_SUBMITTED` | submit_bounty() | Reporter ID, target IP, evidence hash |

---

## STATUS CODES

| Status | TRN Range | Access Level |
|--------|-----------|--------------|
| **GUEST** | #100,000+ | Trade Frequency only |
| **CITIZEN** | #1100-99999 | Trade + Intel Frequency |
| **MERCENARY** | #1100-99999 + Badge | Trade + Intel + Badge |
| **TITAN** | #1024 | All three gates |

---

**"In the mesh, trust is earned. Reciprocity is law."**