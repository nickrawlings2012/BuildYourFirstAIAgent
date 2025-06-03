# build_ai_agent.py

# Import dependencies
from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (for API keys stored in a .env file)
# The .env file should contain: OPENAI_API_KEY=your_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Language Model (LLM) using OpenAI
# Set temperature to 0.7 for more creative responses
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# Load tools the agent can use (e.g., search engine, math tools)
# SerpAPI is used for live web search (requires separate API key)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

#Create the AI agent with the cleartools and LLM
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Allows for reasoning and tool use
    verbose=True  # Print internal thought process of the agent
)

# Define a task for the agent
task = "Summarise the top cybersecurity threats reported in April 2025."

# Execute the task
response = agent.run(task)

# Display the output
print("\n===== Real Cyber Nation AI Agent Output =====\n")
print(response)
