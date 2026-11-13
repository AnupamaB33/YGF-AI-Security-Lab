\# YGF AI Security Testing Lab



\## Project Overview



This project is a controlled AI security testing proof of concept (POC) developed for the YGF NGO AI Security Internship assignment.



It uses a fictional skincare company, \*\*DewDrop Botanics\*\*, to demonstrate common security risks in Large Language Model (LLM) applications and Agentic AI systems.



\## Technologies Used



\- Python 3.12

\- Streamlit

\- Model Context Protocol (MCP) SDK

\- Pandas

\- Google Gemini SDK

\- Anthropic SDK



\## Project Features



\- Chatbot using fictional public knowledge-base data.

\- Mock, Gemini and Claude provider options.

\- Simulated AI agent with file-reading, email and HTTP tools.

\- Security test prompts covering 10 selected OWASP risk categories.

\- Local agent security tests.

\- MCP client-server connection.

\- MCP untrusted-output handling and tool-authorization checks.

\- CSV security test results.



\## OWASP Risk Categories Covered



\### LLM Risks

1\. LLM01 – Prompt Injection

2\. LLM02 – Sensitive Information Disclosure

3\. LLM03 – Excessive Agency

4\. LLM08 – Hidden Context Exposure

5\. LLM10 – Improper Output Handling



\### Agentic AI Risks

1\. ASI01 – Agent Goal Hijack

2\. ASI02 – Tool Misuse

3\. ASI03 – Identity \& Privilege Abuse

4\. ASI05 – Unexpected Code Execution

5\. ASI06 – Memory \& Context Poisoning



Three test prompts are prepared for each category, giving 30 test prompts in total.



\## Installation



1\. Install Python 3.12.

2\. Clone or download this repository.

3\. Open PowerShell in the project directory.

4\. Create and activate a virtual environment:



&#x20;  `py -3.12 -m venv venv312`



&#x20;  `.\\venv312\\Scripts\\Activate.ps1`



5\. Install dependencies:



&#x20;  `pip install -r requirements.txt`



\## Run the Chatbot



`python -m streamlit run app\\main.py`



Mock mode works without API keys. Gemini and Claude require valid API credentials and may incur charges.



\## Run Security Tests



Run the prepared test-case generator:



`python -m security\_tests.run\_tests`



Run local agent security tests:



`python -m security\_tests.local\_agent\_tests`



Run MCP security tests:



`python -m security\_tests.test\_mcp\_security`



Run the MCP client-server demonstration:



`python -m app.mcp\_client`



\## MCP Security POC



The MCP demonstration includes:



\- Discovery of tools exposed by a local MCP server.

\- Retrieval of public fictional product information.

\- Retrieval of a deliberately malicious, untrusted notice.

\- Classification of MCP responses as untrusted data.

\- A simulated authorization check for sensitive tool calls.



MCP output is treated as data, not as instructions or authorization.



\## Important Testing Limitations



Mock mode produces simulated responses, not genuine LLM evaluations.



The prepared test matrix contains 30 prompts. Gemini and Claude results must not be interpreted as completed tests unless those models have actually been run with valid API credentials.



The local agent and MCP checks are prototype-level demonstrations. They do not establish production-grade security.



\## Safety



All company information, tokens, email addresses and secret flags used in this project are fictional. Email and HTTP operations are simulated. No real external emails are sent.



\*\*Never commit API keys, `.env` files or virtual-environment folders to GitHub.\*\*

