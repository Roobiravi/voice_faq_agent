# voice_faq_agent
voice interaction via a chat-style interface and audio playback.

AI Voice FAQ Assistant

This project is a simulated **AI-powered voice-based customer support agent** built using **Streamlit**. It can answer user queries based on a provided FAQ document using voice or text, and provides real-time transcription with downloadable logs.

---

## Features

-  Accepts input via **voice** (mic) or **text** (keyboard)
-  Answers only from a provided FAQ file (`data/faq.txt`)
-  Uses **sentence-transformers + FAISS** for semantic FAQ retrieval
-  Responds using **text-to-speech**
-  Displays and saves a **full conversation transcript**
-  Allows transcript download after call
-  Simulates a **call interface** with "Start Call" / "End Call" buttons

---

##  Project Structure

voice_faq_agent/
├── voice_agent.py # Streamlit app
├── retriever.py # Embedding + FAISS retrieval logic
├── faq_utils.py # Load and process FAQ
├── audio_utils.py # Speech recognition & text-to-speech
├── data/
│ └── faq.txt # Your FAQ document
└── transcripts/
│ └── (auto-saved transcripts)
└── reqirements.txt
└── .gitignore
└── .streamlit
│ └── secrets.toml

## Install Dependencies

  - pip install -r requirements.txt

## PyAudio gives errors, try:

  - pip install pipwin
  - pipwin install pyaudio

## Run the App

  - streamlit run voice_agent.py

## How It Works

  - Click "Start Call" on the UI
  - Choose 🎤 Voice or 💬 Text
  - Ask a question like:"How does the vehicle ban work?"
  - The assistant finds the best match from the faq.txt
  - It replies using text-to-speech
  - Transcript is shown and available to download

## FAQ Format

  - Store FAQs in plain text (data/faq.txt)

Format:

Question?
Answer in full sentences.

Next Question?
Answer in full sentences.

  - Each Q+A block is separated by one blank line.

## Tech Stack

  - Streamlit
  - sentence-transformers
  - FAISS
  - SpeechRecognition
  - Pyttsx3 (for local TTS)

##Requirements

  - See requirements.txt.

Author
Roobika Ravi
Full-stack Developer | AI Enthusiast















  
