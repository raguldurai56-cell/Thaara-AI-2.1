"""Safe core features with optional integrations kept out of import time."""
import platform
import subprocess


def speak(text):
    """Print a response; optional TTS can be layered on later."""
    print(f"Thaara: {text}")
    return text


def playAssistantSound():
    """No-op fallback for the startup sound."""
    return None


def hotword():
    """Run a hotword listener only when an optional implementation is supplied."""
    return False


def open_application(name):
    """Open a platform application when possible, otherwise report safely."""
    if platform.system() == "Windows":
        try:
            subprocess.Popen(["cmd", "/c", "start", "", name], shell=False)
            return True
        except OSError:
            return False
    return False
