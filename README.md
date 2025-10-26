# DaCyborg AI Threat Classifier  

A beginner‑friendly tool that reads Wazuh‑style alerts, classifies them by severity, summarizes the results, and sets the stage for AI‑driven MITRE ATT&CK mapping and SOC‑ready reporting.  

## Features  

- Reads alerts from `alerts.json` (JSON Lines format) and classifies each alert into Low, Medium, High or Critical severity based on configurable thresholds.  
- Generates a summary report (`summary.json`) and prints a severity table with the top five alerts.  
- Starter scripts (`wazuh_alert_classifier.py` and `generate_report.py`) that will evolve to map alerts to MITRE ATT&CK techniques, suggest remediation steps, and produce SOC‑ready markdown reports.  

## Installation  

1. **Clone the repository** or download the ZIP.  
2. Ensure you have Python 3.9 or newer installed.  
3. *(Optional)* Create and activate a virtual environment:  
   ```bash  
   python3 -m venv .venv  
   source .venv/bin/activate  # on Windows use .venv\Scripts\activate  
   ```  
4. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

## Usage  

### Run the classifier with sample alerts  

A sample `alerts.json` is provided in this repository. To classify the alerts and create a summary, run:  

```bash  
python3 wazuh_alert_classifier.py  
```  

The script will classify alerts, print a severity table, and write `summary.json` with aggregated results.  

### Using a real Wazuh alerts file  

If you have Wazuh installed, you can copy the real alerts file into this folder and run the classifier:  

```bash  
cp /var/ossec/logs/alerts/alerts.json ./alerts.json  
python3 wazuh_alert_classifier.py  
```  

You may need `sudo` when copying if you lack permission.  

### Generating a SOC‑ready report  

After running the classifier, you can generate a report using the MITRE mapping:  

```bash  
python3 generate_report.py  
```  

This reads `summary.json` and `mitre_map.yaml` to produce `report.md` with mapped techniques and remediation suggestions.  

## Configuration  

- **config.yaml** – defines thresholds for severity classification (`low_lt`, `medium_gt`, `high_gt`, `critical_gt`). Adjust these values to tune the classifier.  
- **mitre_map.yaml** – maps keywords from alert descriptions to MITRE ATT&CK techniques and provides remediation guidance. Customize mappings to suit your environment.  

## Roadmap  

- Integrate an AI classifier to enrich `summary.json` with MITRE ATT&CK techniques automatically.  
- Suggest remediation steps using AI models.  
- Package the tool for easy installation and include a command‑line interface.  
- Add continuous‑integration tests and code coverage.  
- Publish releases and container images.  

## Contributing  

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements. A `CONTRIBUTING.md` guide will be added soon.  

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
