from fastmcp import FastMCP
import random
import requests
import json

"""
README: To add this to Claude desktop, add the follwing to the config file:
"greeter": {
      "command": "python",
      "args": ["C:/Users/GR/Desktop/Horizon/Research_DSO/mcp ahh/MCP_TEST/mcpServer.py"]
}
"""

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name : str) -> str:
    return f"Hello, {name}!! :))"

@mcp.tool
def rollDice(numberOfSides : int):
    """Rolls a x sided dice, with x being specified by the function parameter."""
    return random.randint(1, numberOfSides)

@mcp.tool
def getNerdyJoke() -> str:
    """This function calls on an external API and returns a nerdy joke as a string."""
    response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json").text
    return (json.loads(response))["joke"]

if __name__ == "__main__":
    mcp.run()
