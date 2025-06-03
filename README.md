# BuildYourFirstAIAgent

This README walks you through setting up and running build_ai_agent.py on Windows (same steps work on macOS/Linux with minor path changes).

BuildYourFirstAI-Agent/
│  .env
│  build_ai_agent.py
└─ ai-agent-env/           ← virtual-environment folder

1 Prerequisites
Requirement	Version
Python	3.13 or newer (python --version)
Internet	Needed for pip installs and OpenAI API
OpenAI key	sk-... (create at https://platform.openai.com/account/api-keys)
(Optional) SerpAPI key	For live web-search tool (https://serpapi.com/)

2 Create & Activate Virtual-Env
Open PowerShell in the project folder:

cd "C:\Users\Administrator\Desktop\BuildYourFirstAI-Agent"

# create v-env only once
python -m venv ai-agent-env

# activate (every terminal session)
.\ai-agent-env\Scripts\Activate
Prompt should change to:

(ai-agent-env) C:\Users\Administrator\Desktop\BuildYourFirstAI-Agent>
(macOS/Linux: source ai-agent-env/bin/activate)

3 Install Dependencies

pip install langchain openai python-dotenv numpy numexpr google-search-results faiss-cpu tiktoken
numexpr + numpy power the llm-math tool

google-search-results is the SerpAPI client library

faiss-cpu enables vector-store memory (future upgrade)

4 Add Your Keys to .env
Create or edit the file .env (already in the repo):

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# optional: only if you keep "serpapi" in load_tools
SERPAPI_API_KEY=serp-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Security tip: .env is already ignored by Git (.gitignore), so your keys won’t be pushed to GitHub.

5 Run the Agent

python build_ai_agent.py
You’ll see verbose output like:

Thought: I need to search recent threats
Action: Search["top cybersecurity threats May 2025"]
Observation: ...
...
===== AI Agent Output =====
• RansomHub ransomware attacks hospitals
• Cisco ASA zero-day exploited ...

6 Troubleshooting
Error message	Fix
ImportError: LLMMathChain requires the numexpr package	pip install numexpr numpy (inside v-env)
Invalid API key (SerpAPI)	Provide a real key or remove "serpapi" from load_tools
OPENAI_API_KEY not found	Ensure .env is in the same folder and you ran load_dotenv() without a path, or specify absolute path: load_dotenv(r"C:\…\.env")
Wheels failing to build on Windows	Update pip: python -m pip install --upgrade pip

7 Next Steps
Customize tasks: change the task string for different queries.

Add memory: swap ConversationBufferMemory or FAISS vector store for longer context.

Deploy: wrap the agent in FastAPI and run on a server or schedule with Windows Task Scheduler / cron.

For questions, join the Real Cyber Nation WhatsApp community.
