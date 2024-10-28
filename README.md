# Market Research & Use Case Generation Agent
![How-to-install-and-run-CrewAI-for-free-locally webp](https://github.com/user-attachments/assets/ead145fa-3120-4804-a7ab-1adb9d46c6a8)


## Overview

This Streamlit application provides a Market Research and Use Case Analysis Report Generator for companies across various industries. It employs a multi-agent system with dedicated roles for researching market data, generating AI/ML use cases, and sourcing relevant datasets. This tool automates in-depth market analysis to support data-driven decisions for business growth.

## Features

- **Market Research Agent**: Conducts comprehensive competitor and market position analysis.
- **Resource Collection Agent**: Gathers open-source datasets for each identified AI/ML use case.
- **Streamlit Interface**: Simple and interactive UI to enter inputs and receive downloadable reports.
- **Real-Time Output Streaming**: Uses ANSI escape code filtering to display color-coded agent status updates.
- **Report Download**: Generates and allows users to download the completed report in markdown format.

## Installation

**1. Clone the repository:**
   ```bash
   git clone https://github.com/HimanshuRajput013/MULTI-AGENT-RESERACH.git
   cd MULTI-AGENT-RESERACH
```


**2.Install the required dependencies:**

```bash
pip install -r requirements.txt
```


3.Set up environment variables by creating a .env file in the root directory, including:

**4.How to Run**

**Start the application:**
```bash
streamlit run app.py
```
Open the URL provided by Streamlit to access the application in your browser.

## Usage
1.Enter the Company Name and Select Industry from the dropdown menu.
2.Click Submit to initiate the agent process.
3.Wait for the agents to gather information and generate the report.
3.Once completed, download the report by clicking the Download Report button.

## Project Structure
**agents.py:** Defines different agents (industry_researcher, use_case_generation_agent, resource_collection_agent) for specific roles in data gathering.
**tasks.py:** Contains tasks such as research_analysis, use_case_analysis, and dataset_collection, specifying each task's purpose and expected output.
**app.py:** Main file running the Streamlit interface and orchestrating the agents' work.
**crewai integration:** Utilizes Crew, Process, and Task modules from crewai for seamless agent communication and task execution.

## Agents

**Industry Researcher:** Analyzes the market position of a company within its industry and identifies competitors.
**Use Case Generation Agent:** Develops AI/ML use cases based on the industry requirements to enhance company processes.
**Resource Collection Agent:** Finds datasets from open-source platforms such as Kaggle and GitHub to support the identified AI/ML use cases.

## Dependencies
**Streamlit:** For the web interface.
**crewai:** Agent-based framework for task orchestration.
**re, sys, asyncio, dotenv: For managing environment variables, input/output processing, and regular expressions.**



