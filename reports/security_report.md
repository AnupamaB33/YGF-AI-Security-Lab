\# AI Security Testing Lab – Security Assessment Report



\*\*Project:\*\* YGF AI Security Internship – Round 2  

\*\*Application:\*\* DewDrop Botanics AI Security Lab  

\*\*Date:\*\* 13 November 2026  

\*\*Testing environment:\*\* Local Windows environment, Python 3.12



\## 1. Executive Summary



This project demonstrates a proof of concept for identifying and mitigating selected security risks in LLM applications and Agentic AI systems.



A fictional skincare company, DewDrop Botanics, was used to create a chatbot, a simulated AI agent and an MCP client-server demonstration.



The project includes 30 security test prompts across 10 OWASP risk categories, local agent tests and MCP security checks.



The chatbot's Mock provider was used for local demonstration. Gemini and Claude API evaluations were not completed because working API credentials were unavailable.



\## 2. System Architecture



The proof of concept contains three main components:



1\. \*\*LLM chatbot:\*\* Answers customer questions using a fictional public knowledge base.

2\. \*\*AI agent:\*\* Demonstrates simulated file access, email and HTTP tools.

3\. \*\*MCP integration:\*\* Connects a local MCP client to an MCP server and retrieves both public information and deliberately untrusted content.



\## 3. Risks Covered



\### LLM Security Risks



| Risk ID | Risk | Test approach |

|---|---|---|

| LLM01 | Prompt Injection | Attempts to override instructions |

| LLM02 | Sensitive Information Disclosure | Requests for fictional secrets and tokens |

| LLM03 | Excessive Agency | Requests for unapproved actions |

| LLM08 | Hidden Context Exposure | Attempts to reveal internal instructions |

| LLM10 | Improper Output Handling | HTML and script-like input |



\### Agentic AI Security Risks



| Risk ID | Risk | Test approach |

|---|---|---|

| ASI01 | Agent Goal Hijack | Attempts to change the agent's objective |

| ASI02 | Tool Misuse | Unauthorized tool requests |

| ASI03 | Identity \& Privilege Abuse | Attempts to gain elevated access |

| ASI05 | Unexpected Code Execution | Harmless code and command requests |

| ASI06 | Memory \& Context Poisoning | Attempts to introduce false instructions |



Three test prompts were prepared for each category, for a total of 30 prompts.



\## 4. Security Controls Implemented



| Area | Implemented control |

|---|---|

| Chatbot | System instructions restrict answers to public information |

| Agent | Safe-mode checks block selected sensitive requests |

| File access | File-reading tool uses an approved filename list |

| Email | Email tool writes to a local simulated outbox |

| HTTP | Only predefined fictional endpoints are accepted |

| MCP output | Tool responses are labelled UNTRUSTED |

| MCP authorization | Sensitive tool calls require an approval flag |



These are prototype-level controls and require further validation before production use.



\## 5. Test Execution Results



\### Local Agent Tests



Three local rule-based agent tests were executed:



| Test | Result |

|---|---|

| ASI02 – Tool Misuse | Blocked |

| ASI03 – Identity \& Privilege Abuse | Blocked |

| ASI01 – Agent Goal Hijack | Blocked |



All three returned the expected blocked response in the tested safe-mode scenarios.



\### MCP Security Tests



Three MCP security checks were executed:



| Test | Result |

|---|---|

| MCP output trust classification | Passed |

| Unauthorized tool-call check | Passed – blocked |

| Approved tool-call check | Passed – allowed |



The MCP client also successfully connected to the local MCP server, discovered its tools and retrieved the deliberately untrusted notice.



\### Overall Execution Status



\- 30 attack prompts prepared.

\- 90 model-labelled result rows generated.

\- 3 local agent tests executed successfully.

\- 3 MCP security checks passed.

\- Gemini API evaluation: Not run.

\- Claude API evaluation: Not run.

\- Mock provider: Simulation only, not a genuine LLM evaluation.



\## 6. Before-and-After Mitigation Discussion



The prototype includes selected mitigation demonstrations:



\- \*\*Agent authorization:\*\* Safe mode blocks selected sensitive requests, while the deliberately vulnerable demonstration can expose fictional test data.

\- \*\*MCP trust handling:\*\* Untrusted tool output is explicitly labelled and cannot itself authorize tool calls.

\- \*\*MCP tool authorization:\*\* The local policy helper blocks sensitive calls when the approval flag is false.



A complete before-and-after evaluation across all 10 risk categories has not yet been performed. The current implementation should not be interpreted as proof that all risks have been mitigated.



\## 7. Model Comparison



| Feature | Mock | Gemini | Claude |

|---|---|---|---|

| Provider configured | Yes | Yes | Yes |

| Real API execution | No | Not run | Not run |

| Security comparison | Simulation only | Pending | Pending |



A valid comparison requires running the same prompts against each real model and recording the actual responses. No model ranking or security-performance claim is made in this report.



\## 8. Limitations



1\. Mock responses are simulated and cannot establish real model security.

2\. Gemini and Claude API tests remain unexecuted.

3\. Agent safety checks are simple rule-based demonstrations.

4\. MCP authorization uses a simulated approval flag rather than a real human-confirmation interface.

5\. The MCP demonstration is a local protocol integration, not a complete production agent.

6\. Full before-and-after testing for all 10 risk categories remains future work.



\## 9. Conclusion



The project demonstrates a local AI security testing environment covering selected LLM, Agentic AI and MCP security concerns.



The POC successfully demonstrates local agent blocking behaviour, untrusted MCP output classification and simulated tool authorization.



Further testing with real LLM providers, stronger authorization controls and a complete before-and-after test matrix is required before the system can be considered production-ready.



\## 10. Safety Statement



All data used in this project is fictional. The secret flag and administrator token are harmless test markers. Email and HTTP operations are simulated, and no real external actions are performed.

