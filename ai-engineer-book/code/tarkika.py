"""Shared setup for the examples in Ship Real AI.

Every example in the book starts by importing what it needs from here, so no name is a mystery:

    from tarkika import llm, INSTRUCTIONS, POLICY

Set OPENAI_API_KEY to run the examples against a real model. The book's own checker sets TARKIKA_FAKE=1
instead, which swaps in a scripted stand-in model so the code can be tested without a key.
"""
import json
import os
from pathlib import Path

HERE = Path(__file__).parent

# The system message from Section 3.3, kept in a file of its own (Section 3.10).
PROMPT_VERSION = "support-v7"
INSTRUCTIONS = (HERE / "prompts" / f"{PROMPT_VERSION}.txt").read_text()

# The five-section return policy used from Module 7 on.
POLICY = (HERE / "data" / "return-policy.md").read_text()

# The eight policy paragraphs P1 to P8 searched in Module 6.
PARAGRAPHS = json.loads((HERE / "data" / "paragraphs.json").read_text())

# A few sample orders. In a real system these live in your order database.
ORDERS = {
    "TK-5521": {"customer_id": "cust-881", "item": "earbuds", "paid": 1499,
                "status": "Delivered on 20 Oct."},
    "TK-6120": {"customer_id": "cust-881", "item": "phone case", "paid": 399,
                "status": "Out for delivery. Expected today by 7 pm."},
    "TK-7004": {"customer_id": "cust-312", "item": "running shoes", "paid": 2899,
                "status": "Delivered on 2 Nov."},
}

# What the assistant says whenever it hands a chat to a person.
HANDOVER = "Thanks for waiting. A person from our support team will reply to you shortly."


def send_for_approval(order_id: str, amount_rupees: int) -> str:
    """Stand-in for your approval queue: a person on the refund team decides."""
    return f"Refund of ₹{amount_rupees} for {order_id} sent to the refund team for approval."


def make_refund(order_id: str, amount_rupees: int) -> str:
    """Stand-in for your payment system."""
    return f"Refund of ₹{amount_rupees} for {order_id} started."


if os.environ.get("TARKIKA_FAKE"):
    from fake_model import ScriptedModel
    llm = small_llm = strong_llm = ScriptedModel()
else:
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-5-mini")         # the main model (Section 1.7)
    small_llm = ChatOpenAI(model="gpt-5-nano")   # small and cheap: summaries, rewrites, grading
    strong_llm = ChatOpenAI(model="gpt-5")       # large: judging answers in Module 9


# Ready-made tools, as built in Section 5.1, for the modules that reuse them.
from langchain_core.tools import tool


@tool
def check_order_status(order_id: str) -> str:
    """Get the delivery status of one order.

    Use this when the customer asks where an order is or when it will
    arrive. order_id looks like TK-5521. Ask the customer for it if you
    do not have it.
    """
    order = ORDERS.get(order_id)
    if order is None:
        return f"No order {order_id} found. Order numbers look like TK-5521."
    return order["status"]


@tool
def search_policy(query: str) -> str:
    """Search Tarkika's return policy and return the most relevant section.

    Use this for questions about returns, refunds, damaged items and hygiene products.
    """
    sections = POLICY.split("\n## ")[1:]
    words = set(query.lower().split())
    return max(sections, key=lambda s: len(words & set(s.lower().split())))


def hybrid_search(query: str, k: int = 5) -> list[str]:
    """A small stand-in for the hybrid search of Section 6.8: ranks P1-P8 by shared words."""
    words = set(query.lower().split())
    ranked = sorted(PARAGRAPHS.values(), key=lambda p: -len(words & set(p.lower().split())))
    return ranked[:k]


# The answer shape from Section 7.6.
from pydantic import BaseModel


class Answer(BaseModel):
    answer: str
    sources: list[str]     # ids of the chunks used, such as "policy-s3"
    found: bool            # False if the sources do not answer the question
