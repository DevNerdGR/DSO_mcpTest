# Structure
- Bridge:
    - Python program to run **MCP server**
    - Interfaces with **Ghidra server** (HTTP server endpoint written in Java, interfaces directly with Ghidra)

- AI Agent --MCP--> bridge program --HTTP--> Java MCP plugin --Ghidra API--> Ghidra



Fork [Ghidra MCP Server](https://github.com/LaurieWired/GhidraMCP) and write custom tools to interface with emulation work.
