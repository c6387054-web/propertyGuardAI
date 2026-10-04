from crewai import Agent, Task, Crew, Process

def create_property_guard_crew(document_text):
    # 1. Document Analysis Agent
    doc_analyzer = Agent(
        role="Document Analysis Specialist",
        goal="Extract key details like Owner Name, Property ID, Area, and Location from property documents.",
        backstory="An expert legal analyst specialized in reading land records and deeds.",
        verbose=True,
        allow_delegation=False
    )

    # 2. Claim Verification Agent
    claim_verifier = Agent(
        role="Claim Verification Specialist",
        goal="Verify document data against registry standards to catch discrepancies.",
        backstory="An experienced property auditor trained in identifying legal mismatches.",
        verbose=True,
        allow_delegation=False
    )

    # 3. Risk Assessment Agent
    risk_assessor = Agent(
        role="Property Fraud Risk Manager",
        goal="Calculate risk score and flag duplicate or fraudulent claims.",
        backstory="A senior fraud risk officer skilled at assessing real estate vulnerabilities.",
        verbose=True,
        allow_delegation=False
    )

    # Tasks Setup
    task1 = Task(
        description=f"Analyze the following property text and extract key structural information:\n{document_text}",
        expected_output="Extracted details: Owner Name, Property ID, Area, Location.",
        agent=doc_analyzer
    )

    task2 = Task(
        description="Verify extracted property details and calculate a Fraud Risk Score (0-100%).",
        expected_output="Risk percentage and risk flags.",
        agent=risk_assessor
    )

    # Crew Setup
    crew = Crew(
        agents=[doc_analyzer, claim_verifier, risk_assessor],
        tasks=[task1, task2],
        process=Process.sequential
    )

    return crew
