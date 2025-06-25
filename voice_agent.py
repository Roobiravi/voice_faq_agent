import streamlit as st
from retriever import FAQRetriever
from faq_utils import load_faq_text
from audio_utils import speech_to_text, text_to_speech
from datetime import datetime
import os

# Set Streamlit app config
st.set_page_config(page_title="AI Voice FAQ Assistant")
st.title("📞 AI Voice FAQ Assistant")
st.markdown("Simulated voice support call interface. Click **Start Call** to begin a session.")

# Load FAQ retriever (cached)
@st.cache_resource
def get_retriever():
    return FAQRetriever(load_faq_text("data/faq.txt"))

retriever = get_retriever()

# Call session state
if "call_active" not in st.session_state:
    st.session_state.call_active = False

# Simulated Call UI
if not st.session_state.call_active:
    if st.button("📲 Start Call"):
        st.session_state.call_active = True
        st.rerun()  # 🔁 Rerun immediately to show call UI
else:
    st.success("Call started! Select input mode and ask your question.")

    # 🎛 Input mode selection
    mode = st.radio("Select input method:", ["🎤 Voice", "💬 Text"], index=1)
    user_input = ""

    if mode == "🎤 Voice":
        st.info("Listening... Speak clearly into your mic.")
        user_input = speech_to_text()
        st.write(f"🗣️ You said: `{user_input}`")
    else:
        user_input = st.text_input("You (typed):", placeholder="e.g. How does the vehicle ban work?")

    # 🚀 Submit button
    if st.button("Submit"):
        if user_input.strip():
            answer, score = retriever.query(user_input)
            print("🔍 User Question:", user_input)
            print("📘 Top Match from FAQ:", answer)
            print("📈 Similarity Score:", score)

            if answer:
                response_text = answer
            else:
                response_text = "I do not have an answer to that question, let me transfer your call to the live agent."

            text_to_speech(response_text)

            # Show + Save transcript
            st.subheader("📜 Full Transcript")
            st.write(f"**User:** {user_input}")
            st.write(f"**Agent:** {response_text}")

            os.makedirs("transcripts", exist_ok=True)
            filename = f"transcripts/transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"User: {user_input}\nAgent: {response_text}\n")
            with open(filename, "rb") as f:
                st.download_button("📥 Download Transcript", f, file_name=os.path.basename(filename))
        else:
            st.warning("Please provide input before submitting.")

    # 🔴 End Call
    if st.button("🔴 End Call"):
        st.session_state.call_active = False
        st.success("Call ended.")
        st.rerun()
