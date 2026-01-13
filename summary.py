import json

with open("analysis.json", "r") as f:
    data = json.load(f)

for domain, details in data.items():
    print(f"{domain}:")
    print("  Strengths:", ", ".join(details["strengths"]))
    print("  Limitations:", ", ".join(details["limitations"]))
    print()