import json
import requests
import yaml

with open("agentConfig.yaml", "r") as file:
    config = yaml.safe_load(file)

OPENROUTER_API_KEY = "sk-YOUR-OPENROUTER-KEY"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_agent(model, role, task):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": f"You are a {role}."},
                     {"role": "user", "content": task}]
    }
    response = requests.post(OPENROUTER_API_URL, headers=headers, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    task = "Bina strategi pemasaran untuk produk digital AI."
    for agent in config["agents"]:
        print(f"--- {agent['name']} ({agent['model']}) ---")
        output = call_agent(agent["model"], agent["role"], task)
        print(output)
        print()