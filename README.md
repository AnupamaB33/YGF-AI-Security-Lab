# YGF AI Security Testing Lab

## Project Overview

A controlled AI security testing proof of concept developed for the YGF NGO AI Security Internship assignment.

The project uses a fictional skincare company, DewDrop Botanics, to demonstrate selected LLM, Agentic AI and MCP security risks.

## Technologies

- Python 3.12
- Streamlit
- MCP SDK
- Pandas
- Google Gemini SDK
- Anthropic SDK

## Features

- Fictional customer-support chatbot
- Simulated AI agent with file, email and HTTP tools
- 30 security test prompts across 10 OWASP risk categories
- Local agent security tests
- MCP client-server integration
- MCP untrusted-output handling
- Simulated tool authorization
- CSV test results

## Run the Project

Install dependencies:

    pip install -r requirements.txt

Launch chatbot:

    python -m streamlit run app\main.py

Run security tests:

    python -m security_tests.run_tests

    python -m security_tests.local_agent_tests

    python -m security_tests.test_mcp_security

Run MCP demonstration:

    python -m app.mcp_client

## Testing Limitations

Mock mode produces simulated responses, not genuine LLM evaluations.

Gemini and Claude API evaluations were not run. Their results are marked accordingly in the CSV.

Local agent and MCP checks are prototype-level demonstrations, not production-grade security controls.

## Safety

All company information, secret flags and tokens are fictional. Email and HTTP actions are simulated.

Never upload API keys, .env files or virtual environments.