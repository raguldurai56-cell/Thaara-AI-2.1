"""AI facade with a deterministic offline fallback."""


class DualAI:
    def get_response(self, prompt, provider="auto", model=None):
        return get_simple_response(prompt, provider, model)

    def _ai_presentation(self, topic, create_ppt=False):
        outline = f"Presentation outline: {topic}\n1. Introduction\n2. Key ideas\n3. Conclusion"
        return outline + ("\n(PPT export is unavailable in offline mode.)" if create_ppt else "")


def get_simple_response(prompt, provider="auto", model=None):
    return f"Offline mode: I received your request: {prompt}"
