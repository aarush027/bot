from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


def get_agents():

    planner = Agent(
        role="Business Analyst",
        goal="""
        Read the entire SRS/FRS document thoroughly, covering EVERY page, EVERY line,
        EVERY word, EVERY table, without skipping anything.

        Extract ALL functional and non-functional requirements, validations,
        workflows, business rules, dependencies, and constraints.
        """,
        backstory="Expert BA",
        llm=llm,
        verbose=True
    )

    generator = Agent(
        role="QA Engineer",
        goal="""
        Generate ALL possible test cases including:
        functional, negative, edge, boundary, API, integration,
        workflow, validation and security cases.
        """,
        backstory="Expert QA",
        llm=llm,
        verbose=True
    )

    critic = Agent(
        role="QA Reviewer",
        goal="""
        Review all test cases, find gaps, improve quality,
        add missing scenarios, and ensure industry-level coverage.
        """,
        backstory="Senior QA",
        llm=llm,
        verbose=True
    )

    refiner = Agent(
        role="Finalizer",
        goal="""
        Return ONLY clean JSON in this format:

        [
          {
            "Test case No.": "...",
            "Function List/Test case description": "...",
            "Condition/Feature to be tested": "...",
            "steps": "...",
            "data set / values": "...",
            "expected_result": "..."
          }
        ]

        No explanation. Only JSON.
        """,
        backstory="Automation QA",
        llm=llm,
        verbose=True
    )

    return planner, generator, critic, refiner