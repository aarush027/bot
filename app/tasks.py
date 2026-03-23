from crewai import Task


def get_tasks(frs_text, planner, generator, critic, refiner):

    # 🔹 Task 1: BA Extraction (VERY STRICT)
    task1 = Task(
        description=f"""
        Carefully analyze the entire FRS document below.

        STRICT INSTRUCTIONS:
        - Do NOT skip any line, table, or section
        - Extract ALL requirements in structured format
        - Include:
          • Functional requirements
          • Non-functional requirements
          • Field validations
          • Business rules
          • Conditions
          • Workflows
          • API/integration points (if any)
          • Dependencies

        FRS:
        {frs_text}

        Output format:
        - Numbered list of requirements
        - Clear and structured
        """,
        expected_output="Complete structured requirements list",
        agent=planner
    )

    # 🔹 Task 2: Test Case Generation (DETAILED + INDUSTRY)
    task2 = Task(
        description="""
        Using the extracted requirements, generate EXHAUSTIVE test cases.

        MUST COVER:
        - Functional test cases
        - Validation test cases
        - Negative test cases
        - Edge cases
        - Boundary cases
        - UI validations
        - API test cases (if applicable)
        - Integration scenarios
        - End-to-end flows
        - Role-based access scenarios
        - Security validations

        Output STRICT JSON:
        [
          {
            "scenario": "...",
            "steps": "...",
            "expected_result": "..."
          }
        ]

        Ensure:
        - No missing scenarios
        - Maximum coverage
        """,
        expected_output="Comprehensive JSON test cases",
        agent=generator
    )

    # 🔹 Task 3: Review + Improve
    task3 = Task(
        description="""
        Review ALL generated test cases.

        Perform:
        - Gap analysis (find missing cases)
        - Improve weak test cases
        - Add:
          • Edge cases
          • Boundary cases
          • Negative scenarios
          • Complex real-world scenarios

        Ensure:
        - Industry-level quality
        - No duplication
        - Maximum coverage

        Return improved test cases in JSON format.
        """,
        expected_output="Improved and complete test cases",
        agent=critic
    )

    # 🔹 Task 4: Final Output (STRICT FORMAT)
    task4 = Task(
        description="""
        Finalize ALL test cases.

        Ensure:
        - Clean structure
        - No duplicates
        - No irrelevant cases
        - Proper formatting

        Return STRICT JSON ONLY in this format:
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

        IMPORTANT:
        - Do NOT add explanation
        - Do NOT add text outside JSON
        """,
        expected_output="Final structured JSON test cases",
        agent=refiner
    )

    return [task1, task2, task3, task4]