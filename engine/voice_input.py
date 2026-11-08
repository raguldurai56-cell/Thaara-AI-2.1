"""Reliable online/offline microphone input.

Online mode uses Google's free SpeechRecognition endpoint. Offline mode uses
Vosk when a local model is installed. Both are optional so the app can still
start without a microphone or speech package.
"""
import os
import time


class VoiceInput:
    def __init__(self):
        self.last_error = ""

    def listen_and_transcribe(self, mode="auto", language="en-IN", timeout=8, phrase_time_limit=8, retries=2):
        mode = (mode or os.getenv("VOICE_MODE", "auto")).lower()
        try:
            import speech_recognition as sr
        except ImportError:
            self.last_error = "Install SpeechRecognition and PyAudio first."
            return ""

        recognizer = sr.Recognizer()
        # These settings make quiet speech easier to detect while limiting noise.
        recognizer.dynamic_energy_threshold = True
        recognizer.energy_threshold = 180
        recognizer.pause_threshold = 0.8
        recognizer.non_speaking_duration = 0.4
        recognizer.phrase_threshold = 0.15

        for attempt in range(max(1, retries + 1)):
            try:
                with sr.Microphone() as source:
                    print("Mic: calibrating background noise...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.8)
                    recognizer.energy_threshold = max(100, recognizer.energy_threshold * 0.75)
                    print("Mic: listening...")
                    audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

                if mode in ("offline", "auto"):
                    text = self._offline(audio, language)
                    if text:
                        return text
                    if mode == "offline":
                        return ""
                if mode in ("online", "auto"):
                    text = recognizer.recognize_google(audio, language=language)
                    if text and text.strip():
                        return text.strip()
            except sr.WaitTimeoutError:
                self.last_error = "No speech detected before timeout."
            except sr.UnknownValueError:
                self.last_error = "Speech was not clear enough."
            except sr.RequestError as exc:
                self.last_error = f"Online speech service unavailable: {exc}"
                if mode == "online":
                    return ""
            except (OSError, AttributeError) as exc:
                self.last_error = f"Microphone unavailable: {exc}"
                return ""
            except Exception as exc:
                self.last_error = str(exc)
            if attempt < retries:
                time.sleep(0.25)
        print(f"Mic: {self.last_error}")
        return ""

    @staticmethod
    def _offline(audio, language):
        model_path = os.getenv("VOSK_MODEL_PATH", "").strip()
        if not model_path:
            return ""
        try:
            import json
            import vosk
            import speech_recognition as sr
            model = vosk.Model(model_path)
            recognizer = vosk.KaldiRecognizer(model, 16000)
            wav = audio.get_wav_data(convert_rate=16000, convert_width=2)
            recognizer.AcceptWaveform(wav)
            return json.loads(recognizer.FinalResult()).get("text", "").strip()
        except Exception:
            return ""


voice_input = VoiceInput()


def listen_and_transcribe(mode="auto", language="en-IN"):
    return voice_input.listen_and_transcribe(mode=mode, language=language)
