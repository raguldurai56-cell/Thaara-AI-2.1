"""Command processing that works offline and is safe by default."""
import urllib.parse
import webbrowser

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


def open_youtube_search(query):
    query = (query or "Tamil songs").strip()
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)
    opened = webbrowser.open(url)
    return speak(f"Opening YouTube search for {query}.") if opened else f"YouTube URL: {url}"


def allCommands(command):
    text = (command or "").strip().lower()
    if not text:
        return "Please provide a command."
    if "system status" in text or "system stats" in text:
        return getSystemStats()
    if "youtube" in text and ("play" in text or "song" in text or "music" in text):
        stop_words = {"open", "youtube", "play", "song", "songs", "music"}
        query = " ".join(word for word in text.split() if word not in stop_words)
        if query == "tamil":
            query = "Tamil songs"
        return open_youtube_search(query or "Tamil songs")
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
