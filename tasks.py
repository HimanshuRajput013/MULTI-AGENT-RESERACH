from crewai import Task
from tools import tool,tool2
from agents import industry_researcher, use_case_generation_agent, resource_collection_agent
# Define Tasks
research_analysis = Task(
    description="Gather detailed market research on {company} in the {industry} industry including competitor",
    expected_output="Comprehensive market report including competitors and strategic focus areas.",
    
    agent=industry_researcher,
    output_file='industry__researcher.md',
    
)

use_case_analysis = Task(
    description="Generate 8-10 AI/ML use cases and benefit in to improve {industry}'s department process for company,aligned with operational goals.",
    expected_output="""Different AI/ML use cases enhance processes and customer satisfaction."
    "format- Use case -'here use case description',
                goal - 'goal of use case', 
                benefit-'how benefit of use case benefit' """
 ,
    
    agent=use_case_generation_agent,
    output_file='use_case_generation__agent.md',
    
)

dataset_collection = Task(
    description="Gather only openable link of 8-10 datasets, datasets desription from github,  kaggle to proposed AI/ML use for {industry}. ",
    expected_output="table format relevant datasets with titles, descriptions, and direct access links.",
    tools=[tool],
    agent=resource_collection_agent,
    output_file='resource_collection__agent.md',
)
