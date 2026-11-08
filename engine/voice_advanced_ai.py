class VoiceAdvancedAI:
    def speak(self, text):
        from .features import speak
        return speak(text)


voice_advanced_ai = VoiceAdvancedAI()
