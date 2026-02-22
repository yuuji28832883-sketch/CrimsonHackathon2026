import requests

ELEVENLABS_API_KEY = "sk_09bc2162234b0d86624fe4688fc7edd77efd45385b16eb1f"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # default voice

def speak_text_to_file(text: str, out_path: str = "output.mp3") -> None:
    print("Sending request to ElevenLabs API...")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {"text": text, "model_id": "eleven_multilingual_v2"}

    r = requests.post(url, json=payload, headers=headers, timeout=60)
    print(f"API response status: {r.status_code}")
    if r.status_code != 200:
        raise RuntimeError(f"ElevenLabs error {r.status_code}: {r.text}")

    with open(out_path, "wb") as f:
        f.write(r.content)

    print(f"Saved: {out_path}")

if __name__ == "__main__":
    print("Starting TTS generation...")
    speak_text_to_file("Hello Yuuji. Your AI assistant is working.")
    print("Done!")