import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text(timeout=5):
    # Simulated speech input
    print("Mock STT activated.")
    return "How does the vehicle ban work?"
