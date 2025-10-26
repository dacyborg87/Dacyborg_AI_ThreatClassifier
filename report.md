# DaCyborg Threat Summary — 2025-10-26T23:15:47.485743Z

## Severity Counts
- **Critical**: 1
- **High**: 1
- **Medium**: 2
- **Low**: 1

## Top Alerts (Enriched)
### [Critical] L12 — Ransomware behavior detected
- **Time**: 2025-10-26T21:11:12.333Z
- **Host/Agent**: dc-server
- **ATT&CK**: T1486 — Data Encrypted for Impact (Tactic: Impact)
- **Suggested Response**:
  Isolate affected host; kill malicious processes; restore from clean backups;
rotate credentials; block IOCs; run full EDR sweep.


### [High] L10 — Suspicious PowerShell execution
- **Time**: 2025-10-26T21:07:42.002Z
- **Host/Agent**: win11-host
- **ATT&CK**: T1059.001 — Command and Scripting Interpreter: PowerShell (Tactic: Execution)
- **Suggested Response**:
  Restrict PowerShell to Constrained Language Mode; enable script block logging;
alert on base64-encoded commands; validate signed scripts only.


### [Medium] L7 — Multiple failed SSH logins
- **Time**: 2025-10-26T21:05:10.555Z
- **Host/Agent**: kali-lab
- **ATT&CK**: T1110 — Brute Force (Tactic: Credential Access)
- **Suggested Response**:
  Enforce MFA; throttle login attempts; block offending IPs; review exposed SSH;
rotate creds; consider port knocking or VPN-only access.


### [Medium] L5 — Possible port scan detected
- **Time**: 2025-10-26T21:09:31.902Z
- **Host/Agent**: suricata-sensor
- **ATT&CK**: T1046 — Network Service Discovery (Tactic: Discovery)
- **Suggested Response**:
  Rate-limit scanning; segment networks; monitor for unusual lateral movement;
block sources at firewall; validate need for open services.


### [Low] L3 — SSH successful login
- **Time**: 2025-10-26T21:00:00.123Z
- **Host/Agent**: ubuntu-web
- **ATT&CK**: N/A — N/A (Tactic: N/A)
- **Suggested Response**:
  (Add playbook step here)
