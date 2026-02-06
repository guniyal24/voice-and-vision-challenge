# 🎙️ The Empathy Engine

> **Giving AI a Human Voice**

A production-ready microservice that bridges the gap between sentiment and sound, transforming emotionally flat text-to-speech into human-like vocal expressions.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00a393.svg)](https://fastapi.tiangolo.com/)

---

## 📖 Overview

In the world of AI interaction, text is smart, but voice is often dumb. Standard Text-to-Speech (TTS) systems fall into the "Uncanny Valley"—they're functional but emotionally flat.

The Empathy Engine solves this by acting as a Translation Layer between sentiment and sound. It detects the emotional intent of user text and dynamically modulates vocal prosody (pitch, speed, volume) to match that feeling.

### ✨ Key Features

- 🧠 Granular Emotion Detection — Uses distilled RoBERTa model to detect 7 distinct emotional states
- 🗣️ Native Prosody Injection — Modifies rate, pitch, and volume at generation level (no DSP distortion)
- ⚡ Asynchronous Architecture — Built on FastAPI with async/await for high performance
- 🎨 Interactive Web Interface — Real-time UI for testing and visualization
- 🎯 Production-Ready — Clean API endpoints ready for integration

---

## 🎨 Screenshots

![Empathy Engine - Joy Detection](./images/empathy-engine-joy.png)

![Empathy Engine - Sadness Detection](./images/empathy-engine-sadness.png)

![Empathy Engine - Anger Detection](./images/empathy-engine-anger.png)

---

## 💡 The Engineering Journey

This project underwent a critical architectural pivot to ensure the highest quality output.

### Phase 1: The DSP Prototype (gTTS + Pydub)

Approach: Generated neutral audio with gTTS, then applied Digital Signal Processing via Pydub.

Problem:

- Joy (high pitch) → Sounded like a "chipmunk" or helium effect
- Sadness (low speed) → Sounded like a "drunk robot" due to sample-rate artifacts

Verdict: ❌ Technically correct, but emotionally broken.

### Phase 2: The Neural Upgrade (Edge-TTS)

Approach: Inject SSML parameters directly into Microsoft Edge Neural TTS.

Result:

- Joy is fast and bright, but retains human timbre
- Sadness is slow and deep, but articulates clearly without slurring

Verdict: ✅ High-fidelity, human-like empathy.

---

## 🎛️ Emotion-to-Voice Mapping

The engine uses deterministic logic to translate semantic intent into acoustic properties:

| Emotion | Rate (Speed) | Pitch | Volume | Rationale |
|---------|--------------|-------|--------|-----------|
| JOY | +20% | +15Hz | +10% | Happiness is energetic with faster speech and higher frequency |
| SADNESS | -15% | -15Hz | -20% | Low energy results in slower speech and lower vocal tension |
| ANGER | +10% | -5Hz | +30% | High arousal (loud/fast) but authoritative (lower/grittier) |
| SURPRISE | +25% | +20Hz | +15% | Shock causes sharp spikes in pitch and tempo |
| FEAR | +15% | +10Hz | 0% | High arousal with tense, erratic speed and high pitch |
| DISGUST | -10% | -10Hz | -10% | Low arousal with vocal distancing |
| NEUTRAL | 0% | 0Hz | 0% | Baseline control |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or 3.11
- Git

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd empathy_engine

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
uvicorn app.main:app --reload
```

You should see:

```
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## 🎮 Usage

### Method A: Web Interface (Recommended)

1. Open your browser to http://127.0.0.1:8000
2. Type a sentence (e.g., "I can't believe you did this, I am so angry!")
3. Click Generate Voice
4. Observe the Detected Emotion badge and diagnostics panel

### Method B: API Endpoint

**POST** `/api/v1/synthesize`

```json
{
  "text": "I finally got the promotion! This is the best day ever!"
}
```

Response:

- Returns a binary .mp3 file
- Custom headers:
  - X-Detected-Emotion: joy
  - X-Modulation-Pitch: +15Hz
  - X-Modulation-Rate: +20%

Example using cURL:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/synthesize" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}' \
  --output output.mp3
```

---

## 📂 Project Structure

```
empathy_engine/
├── app/
│   ├── core/              # Configuration & settings
│   ├── models/            # Pydantic schemas (input/output validation)
│   ├── routers/           # API endpoints
│   ├── services/
│   │   ├── emotion.py     # HuggingFace Transformer logic (the "Brain")
│   │   └── audio.py       # Edge-TTS neural synthesis (the "Mouth")
│   ├── static/            # HTML/CSS/JS for web UI
│   └── main.py            # Application entry point
├── data/                  # Temporary storage for generated audio
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

---

## 🎯 Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Emotion Detection | j-hartmann/emotion-english-distilroberta-base | RoBERTa model for 7-class emotion classification |
| TTS Engine | Microsoft Edge Neural TTS | High-quality neural voice synthesis |
| API Framework | FastAPI | Async/await architecture for performance |
| SSML Processing | edge-tts | Native prosody parameter injection |
| Frontend | Vanilla JS + HTML5 | Lightweight, dependency-free UI |

---

## 🏆 Feature Checklist

- [x] Text input via API and UI
- [x] Emotion detection (7 granular emotions)
- [x] Vocal parameter modulation (rate, pitch, volume)
- [x] Deterministic emotion-to-voice mapping
- [x] Audio output (.mp3 generation)
- [x] Bonus: Granular emotion classification with RoBERTa
- [x] Bonus: Interactive web interface
- [x] Bonus: SSML integration via Edge-TTS

---

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Custom voice selection
- [ ] Emotion intensity scaling
- [ ] Real-time streaming TTS
- [ ] Docker containerization
- [ ] Prometheus metrics integration

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
