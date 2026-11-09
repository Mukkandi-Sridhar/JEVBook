"""Capture the real MCP messages between a client and Tarkika's server (Module 13).

The client launches tools/m13_tee.py, which starts code/tarkika_mcp.py and copies every line passing in either
direction to research/m13-wire.jsonl. The book prints two of those messages exactly as they were sent.
"""
import asyncio
import json
import sys
from pathlib import Path

from mcp import Client, StdioServerParameters

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "research" / "m13-wire.jsonl"


async def main():
    LOG.unlink(missing_ok=True)
    params = StdioServerParameters(command=sys.executable,
                                   args=[str(ROOT / "tools" / "m13_tee.py"), str(LOG)],
                                   cwd=str(ROOT / "code"),
                                   env={"TARKIKA_FAKE": "1", "PATH": "/usr/bin:/bin"})
    async with Client(params) as client:
        tools = await client.list_tools()
        print([t.name for t in tools.tools])
        result = await client.call_tool("check_order_status", {"order_id": "TK-5521"})
        print(result.content[0].text)


asyncio.run(main())
for line in LOG.read_text().splitlines():
    d = json.loads(line)
    print(d["dir"], json.dumps(d["msg"])[:300])
