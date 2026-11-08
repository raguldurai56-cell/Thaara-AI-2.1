"""AI facade with optional Groq/Gemini providers and a free offline fallback."""
import os


def _load_env_file():
    path = ".env"
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"\''))


def _cloud_response(prompt, provider="auto", model=None):
    _load_env_file()
    provider = (provider or "auto").lower()
    if provider in ("auto", "groq") and os.getenv("GROQ_API_KEY"):
        try:
            from groq import Groq
            client = Groq(api_key=os.environ["GROQ_API_KEY"])
            result = client.chat.completions.create(model=model or "llama-3.1-8b-instant", messages=[{"role": "user", "content": prompt}])
            return result.choices[0].message.content
        except Exception:
            if provider == "groq":
                raise
    if provider in ("auto", "gemini") and os.getenv("GEMINI_API_KEY"):
        try:
            import google.generativeai as genai
            genai.configure(api_key=os.environ["GEMINI_API_KEY"])
            result = genai.GenerativeModel(model or "gemini-1.5-flash").generate_content(prompt)
            return result.text
        except Exception:
            if provider == "gemini":
                raise
    return None


class DualAI:
    def get_response(self, prompt, provider="auto", model=None):
        return get_simple_response(prompt, provider, model)

    def _ai_presentation(self, topic, create_ppt=False):
        outline = f"Presentation outline: {topic}\n1. Introduction\n2. Key ideas\n3. Conclusion"
        return outline + ("\n(PPT export is unavailable in offline mode.)" if create_ppt else "")


def get_simple_response(prompt, provider="auto", model=None):
    response = _cloud_response(prompt, provider, model)
    return response or f"Offline mode: I received your request: {prompt}"
