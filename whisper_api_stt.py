import os
from openai import OpenAI
import streamlit as st

# Set API key here 
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def transcribe_with_whisper_api(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

if __name__ == "__main__":
    audio_path = "sample.wav"  # Make sure sample.wav exists in the same folder
    result = transcribe_with_whisper_api(audio_path)
    print("Transcribed text:", result)
