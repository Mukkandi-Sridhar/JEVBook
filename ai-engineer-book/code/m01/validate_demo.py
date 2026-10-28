from typing import Literal
from pydantic import BaseModel, ValidationError

class Ticket(BaseModel):
    category: Literal["refund", "delivery", "product", "other"]
    order_id: str | None = None
    urgent: bool

reply = '{"category": "Refund request", "urgent": true}'
try:
    ticket = Ticket.model_validate_json(reply)
except ValidationError as e:
    print(e.errors()[0]["msg"])
