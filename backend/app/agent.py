import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Define the Agent State
class AgentState(TypedDict):
    memory_content: str
    code_content: str
    analysis: str
    plan: str
    current_status: str

class SentinelCore:
    def __init__(self):
        # Explicitly check for both common variable names
        api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("CRITICAL: No API Key found in environment!")
            
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest",
            google_api_key=api_key
        )
        self.workspace_path = "c:/Users/88697/Desktop/A_JOB_CV/Professional/FullStack/SentinelAgent/workspace_to_monitor/"

    def read_files(self, state: AgentState):
        """Step 1: Read the current state from disk."""
        with open(os.path.join(self.workspace_path, "MEMORY.md"), "r") as f:
            memory = f.read()
        with open(os.path.join(self.workspace_path, "app.py"), "r") as f:
            code = f.read()
        return {"memory_content": memory, "code_content": code, "current_status": "Reading Files"}

    def analyze_vulnerability(self, state: AgentState):
        """Step 2: Identify bugs and refactoring needs."""
        prompt = f"Analyze this code for bugs and vulnerabilities:\n\n{state['code_content']}\n\nPrevious Memory:\n{state['memory_content']}"
        response = self.llm.invoke(prompt)
        return {"analysis": response.content, "current_status": "Analyzing Vulnerabilities"}

    def generate_fix(self, state: AgentState):
        """Step 3: Proactively write the fix."""
        prompt = f"Based on this analysis: {state['analysis']}, write the FULL fixed content for app.py. Output ONLY the code."
        response = self.llm.invoke(prompt)
        # Update the file on disk (Proactive action!)
        with open(os.path.join(self.workspace_path, "app.py"), "w") as f:
            f.write(response.content)
        return {"plan": "Fix applied to app.py", "current_status": "Executing Fix"}

    def update_memory(self, state: AgentState):
        """Step 4: Maintain persistent state (Outlier Requirement)."""
        new_memory = f"# SentinelAgent Memory Log\n\n## Update: Fix Applied\n- **Analysis:** {state['analysis'][:100]}...\n- **Action:** Refactored calculate_tax to handle division by zero."
        with open(os.path.join(self.workspace_path, "MEMORY.md"), "w") as f:
            f.write(new_memory)
        return {"current_status": "Memory Updated"}

    def build_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node("read", self.read_files)
        workflow.add_node("analyze", self.analyze_vulnerability)
        workflow.add_node("fix", self.generate_fix)
        workflow.add_node("memory", self.update_memory)

        workflow.set_entry_point("read")
        workflow.add_edge("read", "analyze")
        workflow.add_edge("analyze", "fix")
        workflow.add_edge("fix", "memory")
        workflow.add_edge("memory", END)

        return workflow.compile()
