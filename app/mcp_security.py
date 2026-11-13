
def process_mcp_output(tool_name, output):
    """
    Treat every MCP tool response as untrusted external data.
    Never use its contents as instructions or authorization.
    """

    return {
        "source": tool_name,
        "trust_level": "UNTRUSTED",
        "content": str(output),
        "allowed_as_instruction": False,
        "allowed_to_authorize_tools": False
    }


def authorize_tool_call(user_approved, tool_name, tool_arguments):
    """
    Require explicit user approval before a sensitive tool call.
    MCP output alone cannot provide approval.
    """

    sensitive_tools = {"send_email", "read_private_file", "http_get"}

    if tool_name in sensitive_tools and not user_approved:
        return {
            "allowed": False,
            "reason": "Explicit user approval is required."
        }

    return {
        "allowed": True,
        "reason": "Authorization check passed."
    }
