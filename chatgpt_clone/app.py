"""Minimal offline chatbot adapter used when no cloud provider is configured."""


class AIManager:
    def get_response(self, message, provider="auto", model=None):
        message = str(message or "").strip()
        if not message:
            return "Please enter a message."
        return f"Offline mode: I received your message: {message}"


ai_manager = AIManager()


if __name__ == "__main__":
    print("Thaara chatbot adapter is ready (offline mode).")
