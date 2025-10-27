# DaCyborg AI Threat Classifier  
  
A beginner-friendly tool that reads Wazuh-style alerts, classifies them by severity, summarizes the results, and sets the stage for AI-driven MITRE ATT&CK mapping, remediation recommendations, and SOC-ready reporting.  
  
## Features  
  
- Classifies alerts from `alerts.json` (JSON Lines format) into Low, Medium, High, or Critical severity using configurable thresholds from `config.yaml`.  
- Generates a summary report (`summary.json`) and prints a severity table with the top five alerts.  
- Provides a script to generate a SOC-ready Markdown report (`generate_report.py`) from `summary.json` and `mitre_map.yaml` that maps alerts to MITRE ATT&CK techniques and suggests remediation steps.  
- **New:** Includes an AI Explainer (`ai_explainer.py`) that uses the OpenAI API to produce a concise threat analysis based on `summary.json`, including an executive summary, likely TTPs, immediate actions, and hardening recommendations.  
  
## Installation  
  
1. Clone the repository or download the ZIP.  
2. Ensure you have Python 3.9 or newer installed.  
3. (Optional) Create and activate a virtual environment:  
  
```bash  
python3 -m venv .venv  
source .venv/bin/activate  # on Windows use .venv\Scripts\activate  
```  
  
4. Install dependencies from `requirements.txt`:  
  
```bash  
pip install -r requirements.txt  
```  
  
### Configure OpenAI (optional)  
  
To use the AI Explainer, you will need an OpenAI API key. Set the `OPENAI_API_KEY` environment variable before running `ai_explainer.py`. You can also set `MODEL_NAME` (default `gpt-4o-mini`).  
  
```bash  
export OPENAI_API_KEY=sk-...    # replace with your key  
export MODEL_NAME=gpt-4o-mini   # optional: choose model  
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
  
### Generate a SOC-ready report  
  
Once you have a `summary.json` file, generate a detailed report that maps alerts to MITRE ATT&CK techniques and suggests remediation guidance:  
  
```bash  
python3 generate_report.py  
```  
  
This reads `summary.json` and `mitre_map.yaml` to produce `report.md` with mapped techniques and remediation suggestions.  
  
### Produce an AI Threat Analysis  
  
After generating `summary.json` (and optionally `report.md`), run the AI Explainer to append an AI-driven analysis:  
  
```bash  
python3 ai_explainer.py  
```  
  
The script reads `summary.json`, builds a prompt describing the top counts and top alerts, sends it to the OpenAI API, and appends the resulting analysis to `report.md` (and writes `analysis.md`). The output includes:  
  
- Executive summary (3–5 sentences)  
- Likely TTPs (bullets)  
- Immediate actions (ordered)  
- Hardening recommendations (bullets)  
  
Make sure your `OPENAI_API_KEY` environment variable is set.  
  
## Configuration  
  
- **config.yaml** – defines thresholds for severity classification (`low_lt`, `medium_gt`, `high_gt`, `critical_gt`). Adjust these values to tune the classifier.  
- **mitre_map.yaml** – maps keywords from alert descriptions to MITRE ATT&CK techniques and provides remediation guidance. Customize mappings to suit your environment.  
  
## Roadmap  
  
- Expand the AI explainer to automatically map alerts to MITRE ATT&CK techniques and enrich `summary.json`.  
- Suggest remediation steps using AI models.  
- Package the tool for easy installation and include a command-line interface.  
- Add continuous-integration tests and code coverage.  
- Publish releases and container images.  
  
## Contributing  
  
Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements. A `CONTRIBUTING.md` guide will be added soon.  
  
## License  
  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
