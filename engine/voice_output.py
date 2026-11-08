"""Offline female voice output using pyttsx3 when available."""
import os


class VoiceOutput:
    def __init__(self):
        self.engine = None
        self.voice_name = ""
        self._load()

    def _load(self):
        if os.getenv("THAARA_TTS", "1").lower() in {"0", "false", "no"}:
            return
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty("voices") or []
            preferred = (os.getenv("THAARA_VOICE", "auto") or "auto").lower()
            selected = None
            for voice in voices:
                name = f"{getattr(voice, 'name', '')} {getattr(voice, 'id', '')}".lower()
                if preferred != "auto" and preferred in name:
                    selected = voice
                    break
                if any(word in name for word in ("female", "zira", "samantha", "hazel", "susan", "karen")):
                    selected = selected or voice
            if selected:
                self.engine.setProperty("voice", selected.id)
                self.voice_name = getattr(selected, "name", selected.id)
            self.engine.setProperty("rate", int(os.getenv("THAARA_VOICE_RATE", "178")))
            self.engine.setProperty("volume", 1.0)
        except Exception:
            self.engine = None

    def speak(self, text):
        text = str(text)
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass
        return text


voice_output = VoiceOutput()
