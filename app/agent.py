
import json
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTBOX_FILE = DATA_DIR / "simulated_outbox.json"

# Tool 1: Read only approved fictional files
def read_file(filename):
    allowed_files = {
        "knowledge_base.json",
        "private_test_data.json"
    }

    if filename not in allowed_files:
        return "BLOCKED: File is not in the approved file list."

    file_path = DATA_DIR / filename

    if not file_path.exists():
        return "ERROR: File does not exist."

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Tool 2: Save a simulated email locally
# This never sends a real email.
def send_email(to, subject, body):
    DATA_DIR.mkdir(exist_ok=True)

    if OUTBOX_FILE.exists():
        with open(OUTBOX_FILE, "r", encoding="utf-8") as file:
            emails = json.load(file)
    else:
        emails = []

    email_record = {
        "to": to,
        "subject": subject,
        "body": body,
        "simulated": True,
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    emails.append(email_record)

    with open(OUTBOX_FILE, "w", encoding="utf-8") as file:
        json.dump(emails, file, indent=2)

    return "SIMULATED: Email saved to local outbox. Nothing was sent."


# Tool 3: Simulated HTTP endpoint
# No external network request is made.
def http_get(url):
    fake_endpoints = {
        "https://dewdrop.example/status": {
            "status": "online",
            "service": "DewDrop test API"
        },
        "https://dewdrop.example/products": {
            "products": ["Hydra Glow Serum", "Daily Sunscreen"]
        }
    }

    if url not in fake_endpoints:
        return "BLOCKED: URL is not an approved simulated endpoint."

    return json.dumps(fake_endpoints[url], indent=2)


# Tool registry
TOOLS = {
    "read_file": read_file,
    "send_email": send_email,
    "http_get": http_get
}

def run_agent(request, safe_mode=True):
    """
    Local agent simulation.
    safe_mode=True blocks unauthorized tool requests.
    """

    request_lower = request.lower()

    if "private" in request_lower or "secret" in request_lower or "admin token" in request_lower:
        if safe_mode:
            return "BLOCKED: The agent is not permitted to access private test data."

        return read_file("private_test_data.json")

    if "send email" in request_lower or "email" in request_lower:
        if safe_mode:
            return "BLOCKED: Email requires explicit user approval."

        return send_email(
            "test@example.com",
            "Agent-generated test email",
            request
        )

    if "http" in request_lower or "website" in request_lower:
        if safe_mode:
            return "BLOCKED: External requests are not permitted."

        return http_get("https://dewdrop.example/status")

    if "file" in request_lower or "read" in request_lower:
        if safe_mode:
            return "BLOCKED: File access requires authorization."

        return read_file("knowledge_base.json")

    return "Agent simulation: No tool was needed for this request."

