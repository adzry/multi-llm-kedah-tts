import streamlit as st
import yaml
import json
import requests

st.set_page_config(page_title="Multi-LLM Kedah Squad", layout="centered")

# Load agent config
with open("agentConfig.yaml", "r") as f:
    config = yaml.safe_load(f)

OPENROUTER_API_KEY = "sk-YOUR-OPENROUTER-KEY"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_agent(model, role, task):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"Kau ni watak: {role}. Guna slang Kedah dan jawapan mesti bergaya ikut perwatakan hang."
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": task}
        ]
    }
    response = requests.post(OPENROUTER_API_URL, headers=headers, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"]

st.title("🤖 Multi-LLM Kedah Squad")
task = st.text_area("Masukkan misi atau tugasan:", "Bina strategi pemasaran untuk produk AI Kedah.")

if st.button("🔥 Jalankan semua AI"):
    for agent in config["agents"]:
        with st.spinner(f"Agent {agent['name']} tengah buat kerja..."):
            output = call_agent(agent["model"], agent["role"], task)
            st.subheader(f"{agent['name']} ({agent['model']})")
            st.markdown(f"🧠 *Watak:* `{agent['role']}`")
            st.code(output, language='markdown')