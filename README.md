# voice_faq_agent
voice interaction via a chat-style interface and audio playback.

AI Voice FAQ Assistant

The AI Voice FAQ Assistant is built to simulate a customer support voice agent that can answer queries based on a structured FAQ document. It combines streaming audio input/output, semantic search, and a real-time interface to handle customer conversations.

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

## System Components

  Layer	          |        Components	                                  |       Description
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Interface	      |       Streamlit UI	                                |    Simulated call interface with Start/End buttons and voice/text input
 NLP Engine	      |       sentence-transformers + FAISS	                |    Embeds the FAQ text and retrieves the most relevant answer based on semantic similarity
 Speech	          |       speech_recognition (STT), pyttsx3 (TTS)	      |    Converts user voice input to text and agent responses back to speech
 Knowledge Base	  |       faq.txt	                                      |    Preprocessed version of the FAQ PDF, organized as Q&A paragraphs
 Transcripts	    |       .txt files                                    |   	Each call's conversation is saved locally and can be downloaded from the UI

## How It Works

  - Click "Start Call" on the UI
  - Choose 🎤 Voice or 💬 Text
  - Ask a question like:"How does the vehicle ban work?"
  - The assistant finds the best match from the faq.txt
  - It replies using text-to-speech
  - Transcript is shown and available to download

## FAQ Format

  - Store FAQs in plain text (data/faq.txt)

## Error Handling

  - Mic access or STT failure → Shows a clear warning
  - Unrecognized audio → Returns fallback message
  - Missing FAQ or formatting issues → Handled during FAQ parsing
  - Network services like OpenAI APIs → Handled via fallback STT option

## Format:

Question?
Answer in full sentences.

Next Question?
Answer in full sentences.

  - Each Q+A block is separated by one blank line.

## Tech Stack

  - Python 3.12
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















  
