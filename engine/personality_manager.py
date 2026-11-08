class PersonalityManager:
    def __init__(self):
        self.response_style = "Professional"
        self.personality = "Formal"

    def set_response_style(self, style):
        self.response_style = str(style)
        return self.response_style

    def set_personality(self, personality):
        self.personality = str(personality)
        return self.personality

    def get_current_settings(self):
        return {"response_style": self.response_style, "ai_personality": self.personality}


personality_manager = PersonalityManager()
