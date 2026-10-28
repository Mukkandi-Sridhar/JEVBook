from typing import Literal
from pydantic import BaseModel, ValidationError


class Ticket(BaseModel):
    category: Literal["refund", "delivery", "product", "other"]
    order_id: str | None = None
    urgent: bool


class BadReply(Exception):
    pass


def parse_ticket(reply: str) -> Ticket:
    try:
        return Ticket.model_validate_json(reply)
    except ValidationError as e:
        raise BadReply(reply) from e
