from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool
from ai_driven_infrastructure_compliance_and_drift_detection.tools.slack_notifier import slack_notifier

@CrewBase
class AiDrivenInfrastructureComplianceAndDriftDetectionCrew():
    """AiDrivenInfrastructureComplianceAndDriftDetection crew"""


    @agent
    def drift_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['drift_analyzer'],
        )

    @agent
    def notification_sender(self) -> Agent:
        return Agent(
            config=self.agents_config['notification_sender'],
            tools=[slack_notifier],
        )


    @task
    def analyze_drift_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_drift_task'],
        )

    @task
    def send_notification_task(self) -> Task:
        return Task(
            config=self.tasks_config['send_notification_task'],
 
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AiDrivenInfrastructureComplianceAndDriftDetection crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
