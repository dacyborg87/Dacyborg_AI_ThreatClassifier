# DaCyborg AI Threat Classifier (Starter)

Welcome DJ! This is a beginner-friendly starter project you can run in minutes.

## What this does
- Reads Wazuh-style alerts from `alerts.json` (JSON Lines format).
- Classifies each alert into Low / Medium / High / Critical based on Wazuh `level`.
- Prints a severity summary and the top 5 alerts.
- Saves a `summary.json` we will use in the next AI step (LLM classification + remediation tips).

## How to run (Mac, very beginner-friendly)

1) **Open Terminal** (Spotlight → type "Terminal").  
2) **Go to your Downloads folder** (or wherever you saved this project):  
   ```bash
   cd ~/Downloads
   ```
3) **Unzip the project** (if you downloaded the ZIP):  
   - Double-click the ZIP, or run:  
     ```bash
     unzip DaCyborg_AI_ThreatClassifier.zip -d DaCyborg_AI_ThreatClassifier
     cd DaCyborg_AI_ThreatClassifier
     ```
   If you're not using the ZIP and just copied the files, `cd` into the project folder.

4) **Run the script**:  
   ```bash
   python3 wazuh_alert_classifier.py
   ```

You should see a severity table and a list of top alerts. A file called `summary.json` will be created.

## Using a real Wazuh alerts file (optional)
If you have Wazuh installed, you can copy the real alerts file into this folder:
```bash
# Adjust the source path if needed:
cp /var/ossec/logs/alerts/alerts.json ./alerts.json
python3 wazuh_alert_classifier.py
```

> Tip: You'll need permission to read Wazuh logs. If the copy fails, prepend `sudo` and enter your password.

## Next step
We’ll add an **AI classifier** to read `summary.json` and:
- Map likely MITRE ATT&CK techniques
- Suggest remediation steps
- Generate a SOC-ready markdown report

Keep this folder — we’ll build on it next.
