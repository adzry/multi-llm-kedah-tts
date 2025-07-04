import requests

def translate_to_slang(text, region="kedah"):
    slang_map = {
        "kedah": {
            "saya": "aku", "anda": "hang", "pergi": "pi", "makan": "makan la", 
            "bagaimana": "macam mana", "di mana": "kat mana", "apa": "pa", "kenapa": "pasai pa"
        },
        "kl": {
            "saya": "saya", "anda": "awak", "pergi": "pergi", "makan": "makan",
            "bagaimana": "macam mana", "di mana": "di mana", "apa": "apa", "kenapa": "kenapa"
        },
        "sabah": {
            "saya": "sia", "anda": "ko", "pergi": "pigi", "makan": "makan bah",
            "bagaimana": "macam mana laitu", "di mana": "di mana bah", "apa": "apa bah", "kenapa": "kenapa bah"
        }
    }
    for k, v in slang_map.get(region, {}).items():
        text = text.replace(k, v)
    return text

def get_tts(text, voice_id, elevenlabs_api_key):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": elevenlabs_api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.7
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(response.content)
        print("✅ Audio generated and saved as voice.mp3")
    else:
        print("❌ Failed to get TTS:", response.text)