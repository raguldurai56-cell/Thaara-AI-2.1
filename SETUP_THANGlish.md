# Thaara AI 2.1 – quick setup

## API key enga add pannanum?

`.env.example`-a copy panni project root-la `.env` create pannunga:

```bash
cp .env.example .env
```

Then:

```env
GROQ_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

`.env` GitHub-ku pogathu; `.gitignore` protect pannum.

## Face + hand sign mode

Basic app API key illama work aagum. Webcam gestures enable panna:

```env
THAARA_GESTURES=1
```

Optional free packages:

```bash
pip install opencv-python mediapipe
```

MediaPipe illa na app crash aagathu; face detection mattum available irundha use pannum.

## Mic strong mode + online/offline AI

UI-la **Online + Offline** mode default. Mic noise calibration, retry, dynamic
threshold, 8-second listening, and clearer pause detection add pannirukku.

```bash
pip install SpeechRecognition PyAudio
```

Online voice recognition-ku internet thevai. Offline voice-ku free Vosk model
download panni `.env`-la path set pannunga:

```env
VOICE_MODE=auto
VOSK_MODEL_PATH=/path/to/vosk-model-small-en-us
```

AI-ku `AI_MODE=auto` use pannunga. First Groq/Gemini key try pannum; key illa na
local Ollama try pannum; adhuvum illa na safe offline response kudukkum.

Free local AI option:

```env
AI_MODE=auto
OLLAMA_MODEL=llama3.2:3b
```

Ollama install panni `ollama pull llama3.2:3b` run pannina, API key illama local
AI work aagum.
