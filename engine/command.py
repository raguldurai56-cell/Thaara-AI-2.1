"""Command processing that works offline and is safe by default."""
from .features import speak
from .system_monitor import getSystemStats

_continuous_listening = False


class EmotionSystem:
    enabled = False

    def enable(self):
        self.enabled = True
        return "Emotion detection enabled"

    def disable(self):
        self.enabled = False
        return "Emotion detection disabled"

    def get_status(self):
        return "Enabled" if self.enabled else "Disabled"


emotion_system = EmotionSystem()


def allCommands(command):
    text = (command or "").strip().lower()
    if not text:
        return "Please provide a command."
    if "system status" in text or "system stats" in text:
        return getSystemStats()
    if text in {"hello", "hi", "hey"}:
        return speak("Hello. I am ready to help.")
    response = f"I received: {command}"
    return speak(response)


def start_continuous_listen():
    global _continuous_listening
    _continuous_listening = True
    return "Continuous listening enabled"


def stop_continuous_listen():
    global _continuous_listening
    _continuous_listening = False
    return "Continuous listening disabled"


def get_continuous_listen_status():
    return "Enabled" if _continuous_listening else "Disabled"
