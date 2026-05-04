from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent import SentinelCore

app = FastAPI(title="SentinelAgent DevSecOps API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sentinel = SentinelCore()
graph = sentinel.build_graph()

@app.get("/api/health")
def health():
    return {"status": "ok", "agent": "SentinelAgent"}

@app.post("/api/run")
async def run_agent():
    """Trigger the agent's reasoning loop."""
    try:
        result = await graph.ainvoke({"current_status": "starting"})
        return {"status": "Success", "last_action": result["current_status"]}
    except Exception as e:
        print(f"AGENT ERROR: {str(e)}")
        return {"status": "Error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006)
