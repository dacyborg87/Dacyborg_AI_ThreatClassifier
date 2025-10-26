# wazuh_alert_classifier.py
# Reads alerts.json, classifies by severity, logs a summary, saves summary.json.
# Run:  python3 wazuh_alert_classifier.py

import json, yaml
from collections import Counter
from datetime import datetime, timezone
from utils import setup_logging

CONFIG_FILE = "config.yaml"

def load_config(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def classify_severity(level: int, cfg) -> str:
    if level < cfg["low_lt"]:
        return "Low"
    elif cfg["medium_gte"] <= level < cfg["high_gte"]:
        return "Medium"
    elif cfg["high_gte"] <= level < cfg["critical_gte"]:
        return "High"
    else:
        return "Critical"

def parse_alert(line: str, cfg):
    try:
        obj = json.loads(line)
        level = int(obj.get("rule", {}).get("level", 0))
        return {
            "level": level,
            "severity": classify_severity(level, cfg),
            "description": obj.get("rule", {}).get("description", "No description"),
            "timestamp": obj.get("timestamp", ""),
            "agent": obj.get("agent", {}).get("name", "unknown-agent"),
        }
    except json.JSONDecodeError:
        return None

def main():
    cfg = load_config(CONFIG_FILE)
    logger = setup_logging(cfg.get("logging", {}).get("level", "INFO"),
                           cfg.get("logging", {}).get("file"))

    input_file = cfg["input_file"]
    output_summary = cfg["output_summary"]

    logger.info(f"Reading alerts from {input_file}")
    alerts = []
    try:
        with open(input_file, "r") as f:
            for line in f:
                rec = parse_alert(line, cfg)
                if rec:
                    alerts.append(rec)
    except FileNotFoundError:
        logger.error(f"File not found: {input_file}.")
        return

    if not alerts:
        logger.warning("No alerts found.")
        return

    counts = Counter(a["severity"] for a in alerts)
    sev_order = ["Critical", "High", "Medium", "Low"]

    logger.info("Severity counts:")
    for sev in sev_order:
        logger.info(f"  {sev:8} {counts.get(sev, 0)}")

    top = sorted(alerts, key=lambda a: a["level"], reverse=True)[:5]
    logger.info("Top alerts:")
    for a in top:
        logger.info(f"  [{a['severity']:^8}] L{a['level']:>2} | {a['timestamp']} | {a['agent']} | {a['description']}")

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),  # fixed UTC warning
        "counts": dict(counts),
        "top_alerts": top,
    }
    with open(output_summary, "w") as out:
        json.dump(summary, out, indent=2)

    logger.info(f"Saved {output_summary} for the next AI step.")

if __name__ == "__main__":
    main()
