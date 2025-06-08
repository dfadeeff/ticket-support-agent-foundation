from fastapi import APIRouter, BackgroundTasks
from ..services.ai_agent import CustomerSupportAgent

router = APIRouter()
agent = CustomerSupportAgent()


@router.post("/tickets")
async def create_ticket(
        ticket: dict,  # Simple dict for now
        background_tasks: BackgroundTasks
):
    # Start AI agent processing
    background_tasks.add_task(
        agent.process_ticket_continuously,
        ticket.get("id")
    )

    return {"status": "created", "ticket": ticket}


@router.get("/tickets/{ticket_id}/agent-status")
async def get_agent_status(ticket_id: str):
    return await agent.get_processing_status(ticket_id)  # Use the real method


@router.post("/tickets/{ticket_id}/escalate")
async def manual_escalate(ticket_id: str):
    return await agent.escalate_to_human(ticket_id)
