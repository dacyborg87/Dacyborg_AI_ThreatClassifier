# generate_report.py
# Reads summary.json + mitre_map.yaml -> writes report.md (SOC-ready)

import json, yaml
from datetime import datetime

SUMMARY = "summary.json"
MAP = "mitre_map.yaml"
REPORT = "report.md"

def load():
    with open(SUMMARY, "r") as f:
        summary = json.load(f)
    with open(MAP, "r") as f:
        mt = yaml.safe_load(f)
    return summary, mt

def match_mitre(desc: str, m):
    desc_l = desc.lower()
    for r in m.get("rules", []):
        if r.get("keyword", "").lower() in desc_l:
            return r
    return None

def main():
    summary, mt = load()
    counts = summary.get("counts", {})
    top = summary.get("top_alerts", [])

    lines = []
    lines.append(f"# DaCyborg Threat Summary — {datetime.utcnow().isoformat()}Z\n")
    lines.append("## Severity Counts")
    for k in ["Critical","High","Medium","Low"]:
        if k in counts:
            lines.append(f"- **{k}**: {counts[k]}")
    lines.append("")

    lines.append("## Top Alerts (Enriched)")
    for a in top:
        desc = a.get("description","")
        m = match_mitre(desc, mt) or {}
        tech = m.get("technique","N/A")
        name = m.get("name","N/A")
        tactic = m.get("tactic","N/A")
        rem = m.get("remediation","(Add playbook step here)")
        lines.append(f"### [{a['severity']}] L{a['level']} — {desc}")
        lines.append(f"- **Time**: {a.get('timestamp','')}")
        lines.append(f"- **Host/Agent**: {a.get('agent','')}")
        lines.append(f"- **ATT&CK**: {tech} — {name} (Tactic: {tactic})")
        lines.append(f"- **Suggested Response**:\n  {rem}")
        lines.append("")

    with open(REPORT, "w") as f:
        f.write("\n".join(lines))

    print(f"Wrote {REPORT}. You can open and paste to GitHub, or share internally.")

if __name__ == "__main__":
    main()
