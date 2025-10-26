#!/usr/bin/env bash
set -e
python3 wazuh_alert_classifier.py
python3 generate_report.py
echo "Done. Open report.md"
