# 🛡️ SentinelAgent: Autonomous DevSecOps Orchestrator

SentinelAgent is a production-grade AI agent designed to monitor repositories, analyze failing logs, and proactively refactor code to fix vulnerabilities. Built for the modern DevSecOps lifecycle, it leverages **LangGraph** for complex reasoning and **Persistent Memory** for long-term state tracking.

---

## 🚀 Key Features

- **Autonomous Reasoning Loop**: Uses a directed cyclic graph (LangGraph) to perform sequential tasks: `Read` -> `Analyze` -> `Fix` -> `Memory Update`.
- **Proactive Self-Healing**: Automatically identifies bugs (like division-by-zero or security flaws) and writes the fixed code directly to the workspace.
- **Persistent State Tracking**: Implements a `MEMORY.md` log system that allows the agent to remember past actions and analysis across sessions—a critical requirement for autonomous agents.
- **Mission Control Dashboard**: A premium, dark-mode terminal interface built with React to trigger and monitor the agent's orchestration trajectory in real-time.

---

## 🛠️ Tech Stack

- **Agentic Framework**: [LangGraph](https://github.com/langchain-ai/langgraph)
- **LLM Brain**: [Google Gemini 1.5 Flash](https://aistudio.google.com/)
- **Backend**: FastAPI (Python 3.10+)
- **Frontend**: React (Vite, TypeScript, Lucide-React)
- **State Management**: Local File Persistence (`MEMORY.md`)

---

## 📂 Project Structure

```text
SentinelAgent/
├── backend/
│   ├── app/
│   │   ├── agent.py       # LangGraph Orchestration Logic
│   │   └── main.py        # FastAPI Entry Point
│   └── .env               # API Configuration (Excluded from Git)
├── frontend/
│   ├── src/
│   │   ├── pages/         # Mission Control Dashboard
│   │   └── App.tsx        # Routing & Layout
│   └── package.json
└── workspace_to_monitor/  # The target code the agent manages
    ├── app.py             # Active code being refactored
    └── MEMORY.md          # Persistent Agent Memory
```

---

## ⚙️ Setup & Installation

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```
*Note: Ensure your `GOOGLE_API_KEY` is set in the `.env` file.*

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## 🤖 Orchestration Trajectory

1. **Read**: The agent scans the `workspace_to_monitor` for code and past memory.
2. **Analyze**: Gemini identifies logic flaws or security vulnerabilities.
3. **Fix**: The agent generates corrected code and overwrites the target file.
4. **Memory**: The agent logs its decision-making process to `MEMORY.md` to maintain context for future runs.

---

*This project is part of a Senior AI/ML Portfolio by **Mulat Ayinet Tiruye**, demonstrating mastery in Agentic Systems and Autonomous Orchestration.*
