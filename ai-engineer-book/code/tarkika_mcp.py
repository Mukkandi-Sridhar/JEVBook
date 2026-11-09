"""Tarkika's order tools as an MCP server (Module 13). Run it with: python tarkika_mcp.py"""
from mcp.server.mcpserver import MCPServer
from tarkika import ORDERS, POLICY

server = MCPServer("tarkika-orders")

@server.tool()
def check_order_status(order_id: str) -> str:
    """Get the delivery status of one order. order_id looks like TK-5521."""
    order = ORDERS.get(order_id)
    if order is None:
        return f"No order {order_id} found. Order numbers look like TK-5521."
    return order["status"]

@server.resource("policy://returns")
def return_policy() -> str:
    """Tarkika's return policy, all five sections."""
    return POLICY

if __name__ == "__main__":
    server.run()          # stdio: requests on stdin, replies on stdout
