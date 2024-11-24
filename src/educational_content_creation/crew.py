from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ContentCreationCrew():
    """ContentCreationCrew crew"""

    @agent
    def content_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_specialist'],
            
        )

    @agent
    def quiz_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_developer'],
            
        )

    @agent
    def content_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_reviewer'],
            
        )


    @task
    def generate_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_content_task'],
            tools=[],
        )

    @task
    def create_quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_quiz_task'],
            tools=[],
        )

    @task
    def review_content_and_quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_content_and_quiz_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the ContentCreationCrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
