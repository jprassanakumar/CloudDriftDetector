# AI-Driven Infrastructure Compliance & Drift Detection

## Overview

This repository contains an **AI-powered automation system** that detects compliance drift in **Terraform-managed infrastructure** and sends real-time notifications via Slack. It utilizes **CrewAI** to orchestrate the detection and notification workflow.

### Key Features:
- **Automated Terraform Compliance Drift Detection**
- **Works with Any Cloud or On-Prem Infrastructure Managed by Terraform**
- **CrewAI Orchestration for Analysis & Notifications**
- **Real-time Slack Alerts for Drift Remediation**
- **Modular, Easily Extendable Architecture**


---

## How It Works

1. **Drift Analysis**  
   - The **Drift Analyzer Agent** inspects Terraform output and identifies configuration discrepancies.

2. **Notification Dispatch**  
   - If drift is detected, the **Notification Sender Agent** formats the results and sends an alert to a Slack channel.

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- [`crewai`](https://github.com/crewai) package installed
- Terraform CLI installed
- A Slack webhook URL for notifications

### Installation Steps

Clone the repository:

   ```bash
   git clone https://github.com/yourusername/infra-drift-detector.git
   cd infra-drift-detector
```



Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**
### Update the agents.yaml file:
```bash
workflow:
  task:
    slack_notification_endpoint: "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    parameters:
      terraform_directory: "/path/to/your/terraform/project"
      variable_files:
        - "variables.tfvars"
```
## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the ai_driven_infrastructure_compliance_and_drift_detection Crew, assembling the agents and assigning them tasks as defined in your configuration.

