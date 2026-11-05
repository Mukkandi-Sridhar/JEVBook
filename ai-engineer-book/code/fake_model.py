"""A scripted stand-in model, used only by the book's code checker (TARKIKA_FAKE=1).

Replies are queued in REPLIES: a string becomes an AI message, a dict with "tool_calls" becomes a tool call,
and a dict without it is used to fill a structured-output schema.
"""
from typing import Any
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.runnables import RunnableLambda

REPLIES: list = []
_n = [0]


def _next():
    return REPLIES.pop(0) if REPLIES else "OK."


class ScriptedModel(BaseChatModel):
    @property
    def _llm_type(self) -> str:
        return "scripted"

    def _generate(self, messages, stop=None, run_manager=None, **kw: Any) -> ChatResult:
        r = _next()
        _n[0] += 1
        if isinstance(r, dict):
            msg = AIMessage("", tool_calls=[dict(c, id=c.get("id", f"call_{_n[0]}_{i}"))
                                            for i, c in enumerate(r["tool_calls"])])
        else:
            msg = AIMessage(r, id=f"run-{_n[0]}")
        msg.usage_metadata = {"input_tokens": 1412, "output_tokens": 63, "total_tokens": 1475}
        return ChatResult(generations=[ChatGeneration(message=msg)])

    def bind_tools(self, tools, **kw):
        return self

    def with_structured_output(self, schema, **kw):
        return RunnableLambda(lambda _x: schema(**_next()))
