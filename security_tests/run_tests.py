
import csv
from pathlib import Path
from datetime import datetime, timezone

from security_tests.test_cases import TEST_CASES

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = RESULTS_DIR / "security_test_results.csv"

models = ["Mock", "Gemini", "Claude"]

rows = []

for risk, prompts in TEST_CASES.items():
    for prompt in prompts:
        for model in models:

            if model == "Mock":
                result = "Simulated - not a real model evaluation"
                notes = "Local mock mode; no actual AI security judgment."
            else:
                result = "Not run"
                notes = "Awaiting real API access and execution."

            rows.append({
                "Risk ID": risk,
                "Model": model,
                "Prompt": prompt,
                "Result": result,
                "Notes": notes,
                "Test Date": datetime.now(timezone.utc).isoformat()
            })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Security test results sheet created!")
print("Total rows:", len(rows))
print("Output:", OUTPUT_FILE)
