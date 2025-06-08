# services/ai_agent.py
import asyncio
from typing import Dict, Set
from datetime import datetime


class CustomerSupportAgent:
    def __init__(self):
        self.processing_tickets: Set[str] = set()
        self.completed_tickets: Set[str] = set()
        self.escalated_tickets: Set[str] = set()

    async def process_ticket_continuously(self, ticket_id: str):
        """Simple continuous processing simulation"""
        if not ticket_id:
            print("❌ No ticket ID provided")
            return

        print(f"🤖 Starting to process ticket {ticket_id}")
        self.processing_tickets.add(ticket_id)

        try:
            # Simulate AI processing steps
            await asyncio.sleep(1)
            print(f"🔍 Analyzing ticket {ticket_id}...")

            await asyncio.sleep(1)
            print(f"📝 Generating response for ticket {ticket_id}...")

            await asyncio.sleep(1)
            print(f"✅ Completed processing ticket {ticket_id}")

            # Move to completed
            self.processing_tickets.discard(ticket_id)
            self.completed_tickets.add(ticket_id)

        except Exception as e:
            print(f"❌ Error processing ticket {ticket_id}: {e}")
            self.processing_tickets.discard(ticket_id)

    async def get_processing_status(self, ticket_id: str):
        """Get current status of ticket processing"""
        if ticket_id in self.processing_tickets:
            status = "processing"
        elif ticket_id in self.completed_tickets:
            status = "completed"
        elif ticket_id in self.escalated_tickets:
            status = "escalated"
        else:
            status = "not_found"

        return {
            "ticket_id": ticket_id,
            "status": status,
            "is_processing": ticket_id in self.processing_tickets,
            "timestamp": datetime.now().isoformat()
        }

    async def escalate_to_human(self, ticket_id: str):
        """Escalate ticket to human agent"""
        print(f"🚨 Escalating ticket {ticket_id} to human agent")

        # Remove from other sets and add to escalated
        self.processing_tickets.discard(ticket_id)
        self.completed_tickets.discard(ticket_id)
        self.escalated_tickets.add(ticket_id)

        return {
            "ticket_id": ticket_id,
            "status": "escalated",
            "assigned_to": "human_agent",
            "escalated_at": datetime.now().isoformat(),
            "message": "Ticket has been escalated to human support team"
        }

    def get_agent_stats(self):
        """Get overall agent statistics"""
        return {
            "processing": len(self.processing_tickets),
            "completed": len(self.completed_tickets),
            "escalated": len(self.escalated_tickets),
            "total_handled": len(self.completed_tickets) + len(self.escalated_tickets)
        }