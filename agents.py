from crewai import Agent
from crewai import LLM
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool

load_dotenv()

import asyncio

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
# Defining the base llm model

os.environ["GEMINI_API_KEY"] = os.environ.get("GOOGLE_API_KEY")


llm = LLM(model="gemini/gemini-pro",api_key = os.environ["GEMINI_API_KEY"],temperature=0.9)


industry_researcher = Agent(
    role="Market Research Analyst",
    goal="Analyze {company} market position in the {industry} industry, including competitor analysis.",
    verbose=True,
    memory=True,
    backstory=("Experienced market analyst focused on identifying competitors and strategic areas for growth in {industry}."),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)


use_case_generation_agent = Agent(
    role="AI Use Case Developer",
    goal="Identify 8-10 AI/ML applications use and applications benefit to improve {industry} processes for {company}.",
    verbose=True,
    memory=True,
    backstory=("Specialist in AI/ML applications for the {industry} industry, focused on generating impactful use cases."),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

resource_collection_agent = Agent(
    role="Data Resource Aggregator",
    goal="Search  8-10  datasets with link,proposed AI/ML  use in {industry} Kaggle and GitHub.",
    verbose=True,
    memory=True,
    backstory=("Skilled in sourcing datasets with openable links for AI/ML in {industry}  from  Kaggle and GitHub with their link"),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)
