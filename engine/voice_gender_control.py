import json
from pathlib import Path


class VoiceControl:
    def __init__(self):
        self.current_gender = "male"
        self.load_config()

    def load_config(self):
        try:
            self.current_gender = json.loads(Path("voice_config.json").read_text()).get("gender", "male")
        except (OSError, ValueError):
            pass

    def speak_with_gender(self, text):
        from .features import speak
        return speak(text)


voice_control = VoiceControl()
