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
