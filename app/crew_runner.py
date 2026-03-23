from crewai import Crew
from app.agents import get_agents
from app.tasks import get_tasks


def run_agents(frs_text):

    planner, generator, critic, refiner = get_agents()
    tasks = get_tasks(frs_text, planner, generator, critic, refiner)

    crew = Crew(
        agents=[planner, generator, critic, refiner],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    # ✅ FIX: extract real output
    final_output = result.raw

    print("\n===== FINAL OUTPUT =====\n")
    print(final_output)

    return final_output