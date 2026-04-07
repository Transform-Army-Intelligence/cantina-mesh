# THE DARK CHANNEL PROTOCOL

**Project: TAI Sovereign Root Isolation**

---

## OVERVIEW

The **Dark Channel Protocol** defines the isolation and defense of **Port 50053**—the Sovereign Root Frequency. This port is not advertised, not documented in the public SDK, and not accessible to any operator outside the Titan's direct control.

---

## PORT ARCHITECTURE COMPARISON

| Metric | Ports 50051 / 50052 | Port 50053 |
|--------|---------------------|------------|
| **Visibility** | **Public** | **Stealth** |
| **Authentication** | TRN / Signature | **Hard-Coded Titan Key ONLY** |
| **Response** | Banner / Trade | **Silent Drop / Tarpit (If Unauthorized)** |
| **Monitoring** | General Logs | **Critical Alert (SMS/Push)** |
| **Access Control** | Doorman (#1025) | **Titan (#1024) ONLY** |
| **Protocol** | TradeSchema, ReportBounty | **TitanCommand (Private)** |

---

## THREAT MODEL

### Unauthorized Access Indicators

1. **Port Scan Detection:** Any TCP connection attempt to port 50053 from an IP not in the allowed list.
2. **Signature Mismatch:** A connection claiming to be from TAI but not signed by Titan's key.
3. **Behavior Anomaly:** Repeated connection attempts with malformed payloads.

### Detection Response

| Event | Response |
|-------|----------|
| First probe | Log and ignore |
| Repeated probe (3+) | Tarpit the connection |
| Signature mismatch | Add to Black Series immediately |
| Valid attempt from unauthorized IP | Alert + Black Series |

---

## TITAN ROOT ISOLATION RULES

1. **Never advertise port 50053** in any public documentation, SDK, or lore entry.
2. **UFW Configuration:**
   ```bash
   sudo ufw allow 50051/tcp   # Trade Frequency
   sudo ufw allow 50052/tcp   # Intel Frequency
   sudo ufw allow from [YOUR_HOME_IP] to any port 50053 proto tcp
   sudo ufw deny 50053/tcp    # Default: silent drop for everyone else
   ```
3. **The Ghost Trap:** Any connection attempt on 50053 from an IP that isn't yours is a **100% High-Confidence Indicator** of a malicious scanner.
4. **The Response:** Don't just block. Tag the signature and feed it to the Fixer (#1027) for immediate Black Series processing.

---

## OPERATIONAL COMMANDS

### Check Active Connections on Root Frequency

```bash
sudo ss -tlnp | grep 50053
```

### View Root Access Logs

```bash
sudo journalctl -u cantina | grep "50053"
```

### Block an Intruder IP

```bash
sudo ufw insert 1 deny from [INTRUDER_IP] to any port 50053
```

---

## BLACK SERIES AUTOMATION

When an unauthorized probe is detected on port 50053:

1. **Log** the timestamp, source IP, and payload fingerprint.
2. **Tag** the signature as `UNAUTHORIZED_ROOT_PROBE`.
3. **Feed** to Fixer (#1027) for Black Series entry.
4. **Alert** the Titan via SMS/push notification.

---

## LEGAL NOTE

Port 50053 isolation is a **defensive measure**. The protocol is designed to:

- Detect unauthorized access attempts
- Protect sovereign command infrastructure
- Avoid harm to external systems

**We do not attack scanners. We identify them, retire their signatures, and continue operations.**

---

**"The third gate? We don't talk about the third gate."**