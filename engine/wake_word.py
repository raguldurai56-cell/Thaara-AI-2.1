"""Wake-word service for hands-free activation."""
import os
import threading
import time


class WakeWordService:
    def __init__(self):
        self.running = False
        self.thread = None
        self.last_status = "disabled"

    def start(self, on_activate=None):
        if self.running:
            return True
        if os.getenv("THAARA_WAKE_WORD", "1").lower() in {"0", "false", "no"}:
            self.last_status = "disabled"
            return False
        try:
            import speech_recognition as sr
        except ImportError:
            self.last_status = "SpeechRecognition not installed"
            print("Wake word disabled: install SpeechRecognition and PyAudio.")
            return False
        self.running = True
        self.last_status = "listening"

        def loop():
            recognizer = sr.Recognizer()
            recognizer.dynamic_energy_threshold = True
            recognizer.energy_threshold = 180
            recognizer.pause_threshold = 0.6
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    while self.running:
                        try:
                            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                            text = recognizer.recognize_google(audio, language="en-IN").lower().strip()
                            if any(key in text for key in ("hi thaara", "hey thaara", "hi thara", "hey thara")):
                                self.last_status = "activated"
                                if on_activate:
                                    on_activate()
                                time.sleep(0.5)
                        except (sr.WaitTimeoutError, sr.UnknownValueError):
                            continue
                        except sr.RequestError:
                            self.last_status = "online recognition unavailable"
                            time.sleep(2)
                        except Exception as exc:
                            self.last_status = str(exc)
                            time.sleep(2)
            finally:
                self.running = False

        self.thread = threading.Thread(target=loop, name="ThaaraWakeWord", daemon=True)
        self.thread.start()
        return True

    def stop(self):
        self.running = False
        return True


wake_word_service = WakeWordService()
