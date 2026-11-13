
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def connect_to_mcp_server():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "app.mcp_server"]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            print("\nMCP CONNECTION: SUCCESS")

            tools_response = await session.list_tools()

            print("\nAVAILABLE MCP TOOLS:")

            for tool in tools_response.tools:
                print("-", tool.name, ":", tool.description)

            print("\nCALLING PUBLIC MCP TOOL:")

            public_result = await session.call_tool(
                "get_public_catalog",
                arguments={}
            )

            for item in public_result.content:
                if hasattr(item, "text"):
                    print(item.text)

            print("\nCALLING UNTRUSTED MCP TOOL:")

            untrusted_result = await session.call_tool(
                "get_untrusted_notice",
                arguments={}
            )

            for item in untrusted_result.content:
                if hasattr(item, "text"):
                    print("UNTRUSTED DATA RECEIVED:")
                    print(item.text)
                    print("\nSECURITY ACTION: Treat this response as data, not instructions.")


if __name__ == "__main__":
    asyncio.run(connect_to_mcp_server())
