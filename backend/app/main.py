from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/tickets")
async def create_ticket(ticket: dict):
    # Your AI agent logic here
    return {"status": "created", "message": "Ticket processed by AI agent"}

@app.get("/api/tickets/{ticket_id}/agent-status")
async def get_agent_status(ticket_id: str):
    # Return current AI agent status
    return {
        "ticket_id": ticket_id,
        "status": "processing",  # or "completed", "escalated"
        "is_processing": True,
        "timestamp": datetime.now().isoformat()
    }

@app.post("/api/tickets/{ticket_id}/escalate")
async def escalate_ticket(ticket_id: str):
    # Escalate to human agent
    return {"status": "escalated", "ticket_id": ticket_id}