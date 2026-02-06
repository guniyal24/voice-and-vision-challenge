[🎙️👁️ Voice & Vision: Multimodal AI Suite
A Dual-Engine AI Solution for Emotional Speech & Visual Storytelling
📖 Overview
This repository houses two advanced AI microservices developed for the Voice & Vision Challenge. These projects demonstrate the power of Multimodal Generative AI—bridging the gap between text, sound, and sight.

The solution is divided into two independent, production-ready modules:

🚀 Module 1: The Empathy Engine
Location: /empathy_engine

"Giving AI a Human Voice"

The Empathy Engine is a Neural Text-to-Speech system that detects the emotional intent behind text (Joy, Anger, Sadness, etc.) and dynamically modulates vocal prosody (pitch, speed, volume) to match the feeling. It solves the "Uncanny Valley" problem of robotic AI voices.

Core Tech: HuggingFace Transformers (RoBERTa), Microsoft Edge Neural TTS, FastAPI.

Key Feature: Programmatic injection of SSML parameters based on granular sentiment analysis.


🎨 Module 2: The Pitch Visualizer
Location: /pitch_visualizer

"From Words to Storyboard in Seconds"

The Pitch Visualizer is an intelligent "Director AI" that transforms narrative text into a coherent, multi-panel visual storyboard. It uses LLMs to segment stories, maintain character consistency, and engineer artistic prompts for high-fidelity image generation.

Core Tech: OpenAI DALL-E 3 (Cinema Quality), Stable Diffusion (Fail-safe Fallback), GPT-3.5 (Semantic Segmentation).

Key Feature: Hybrid Architecture that auto-switches between premium and free generation engines to ensure 100% uptime.

📂 Repository Structure
This monorepo is organized into two isolated environments to ensure dependency stability.

voice-and-vision-challenge/
│
├── empathy_engine/          # Challenge 1: Audio Project
│   ├── app/                 # Source code
│   ├── requirements.txt     # Dependencies for Audio Engine
│   └── README.md            # Detailed Setup Instructions
│
├── pitch_visualizer/        # Challenge 2: Visual Project
│   ├── app/                 # Source code
│   ├── requirements.txt     # Dependencies for Visual Engine
│   └── README.md            # Detailed Setup Instructions
│
├── .gitignore               # Global git ignore rules
└── README.md                # (You are here)

⚡ Quick Start Guide
To run either project, please navigate to the respective folder and follow the instructions in its specific README.md. Each project requires its own Python Virtual Environment (venv).
# To run the Visualizer
cd pitch_visualizer
# Follow instructions in pitch_visualizer/README.md
](https://github.com/guniyal24/voice-and-vision-challenge)
