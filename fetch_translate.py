
import requests
import json
from datetime import datetime

# Base URLs
ENGLISH_API_URL = "https://aztro.sameerkumar.website/?sign={sign}&day={day}"
TRANSLATE_API_URL = "https://libretranslate.de/translate"

# Horoscope signs
SIGNS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

# Fetch horoscope for one sign
def fetch_english_horoscope(sign, day="today"):
    response = requests.post(ENGLISH_API_URL.format(sign=sign, day=day))
    if response.status_code == 200:
        return response.json().get("description", "")
    return ""

# Translate text to Urdu
def translate_to_urdu(text):
    response = requests.post(TRANSLATE_API_URL, data={
        "q": text,
        "source": "en",
        "target": "ur",
        "format": "text"
    })
    if response.status_code == 200:
        return response.json().get("translatedText", "")
    return ""

# Main script
def main():
    data = {}
    today = datetime.now().strftime("%Y-%m-%d")
    for sign in SIGNS:
        english = fetch_english_horoscope(sign)
        urdu = translate_to_urdu(english)
        data[sign] = {
            "date": today,
            "sign": sign,
            "horoscope_english": english,
            "horoscope_urdu": urdu
        }

    # Save JSON file
    with open("data/daily.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
