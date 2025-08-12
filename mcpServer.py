from fastmcp import FastMCP
import random

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name : str) -> str:
    return f"Hello, {name}!! :))"

@mcp.tool
def rollDice(numberOfSides : int):
    """Rolls a x sided dice, with x being specified by the function parameter."""
    return random.randint(1, numberOfSides)

if __name__ == "__main__":
    mcp.run()
