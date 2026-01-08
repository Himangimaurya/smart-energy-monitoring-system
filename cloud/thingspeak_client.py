import requests
from config.settings import THINGSPEAK_API_KEY, THINGSPEAK_URL


class ThingSpeakClient:
    def upload(self, power, energy):
        """
        Upload data to ThingSpeak cloud
        """
        payload = {
            "api_key": THINGSPEAK_API_KEY,
            "field1": power,
            "field2": energy
        }

        try:
            requests.get(THINGSPEAK_URL, params=payload, timeout=5)
        except Exception as e:
            print("Cloud upload failed:", e)
