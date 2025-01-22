#!/usr/bin/env python
import sys
from ai_driven_infrastructure_compliance_and_drift_detection.crew import AiDrivenInfrastructureComplianceAndDriftDetectionCrew
import subprocess
import yaml


# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def detect_drift(terraform_directory, variable_files):
    try:
        # Build the Terraform command
        terraform_command = ["terraform", "plan", "-detailed-exitcode"]
        
        # Add variable files to the command
        for var_file in variable_files:
            terraform_command.extend(["-var-file", var_file])
        
        # Run the command in the specified Terraform directory
        result = subprocess.run(
            terraform_command,
            cwd=terraform_directory,
            capture_output=True,
            text=True
        )
        
        # Interpret the exit code
        if result.returncode == 2:
            print("Drift detected!")
            print(result.stdout)
            #run(result.stdout)
            return result.stdout
        elif result.returncode == 0:
            print("No drift detected.")
            return {"status": "no_drift", "output": result.stdout}
        else:
            print("Error running Terraform.")
            return {"status": "error", "output": result.stderr}
    except Exception as e:
        print(str(e))
        return str(e)

def load_workflow_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)



#def run(tf_stdout):
def run():
    """
    Run the crew.
    """
    workflow_config = load_workflow_config("./config/agents.yaml")
    terraform_directory = workflow_config["workflow"]["task"]["parameters"]["terraform_directory"]
    variable_files = workflow_config["workflow"]["task"]["parameters"]["variable_files"]
    tf_stdout = detect_drift(terraform_directory, variable_files)
    inputs = {
        'notification_endpoint': workflow_config["workflow"]["task"]["slack_notification_endpoint"],
        'terraform_output': tf_stdout
    }
    AiDrivenInfrastructureComplianceAndDriftDetectionCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'notification_endpoint': 'sample_value'
    }
    try:
        AiDrivenInfrastructureComplianceAndDriftDetectionCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiDrivenInfrastructureComplianceAndDriftDetectionCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'notification_endpoint': 'sample_value'
    }
    try:
        AiDrivenInfrastructureComplianceAndDriftDetectionCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
