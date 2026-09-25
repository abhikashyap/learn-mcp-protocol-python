"""A small MCP server to explore while learning the protocol."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Learning Server")


@mcp.tool()
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to MCP."


@mcp.resource("learning://welcome")
def welcome_resource() -> str:
    """A short resource that MCP clients can read."""
    return "Welcome! Explore tools, resources, and prompts as you learn MCP."


@mcp.prompt()
def explain_mcp(topic: str) -> str:
    """Create a prompt asking for a beginner-friendly explanation."""
    return f"Explain {topic} in beginner-friendly terms, with a small example."


if __name__ == "__main__":
    mcp.run()
