import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import speech_recognition as sr
import pyttsx3

from gemini_utility import (
    load_gemini_model,
    gemini_text_response,
    gemini_vision_response,
    embeddings_model_response
)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Gemini AI Suite",
    page_icon="🧠",
    layout="wide"
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🧠 Gemini AI Suite")
    selected = option_menu(
        menu_title=None,
        options=[
            "ChatBot",
            "Image Captioning",
            "Text Embeddings",
            "Ask Anything",
            "Voice Assistant"
        ],
        icons=["chat-dots", "image", "braces", "question-circle", "mic"],
        default_index=0,
    )
    st.markdown("---")
    st.caption("Built with Google Gemini + Streamlit")

# ---------- ROLE MAP ----------
def role_map(role):
    return "assistant" if role == "model" else role

# ---------- VOICE FUNCTIONS ----------
def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak now")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# ================= CHATBOT =================
if selected == "ChatBot":

    st.title("💬 Gemini Chat Assistant")

    model = load_gemini_model()

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("🗑 Clear"):
            st.session_state.chat_session = model.start_chat(history=[])
            st.rerun()

    for msg in st.session_state.chat_session.history:
        with st.chat_message(role_map(msg.role)):
            st.markdown(msg.parts[0].text)

    user_input = st.chat_input("Type your message...")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Gemini thinking..."):
            response = st.session_state.chat_session.send_message(user_input)

        with st.chat_message("assistant"):
            st.markdown(response.text)


# ================= IMAGE CAPTIONING =================
elif selected == "Image Captioning":

    st.title("🖼️ AI Image Captioning")

    uploaded = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:
        image = Image.open(uploaded)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(image, caption="Uploaded Image")

        with col2:
            st.markdown("### Caption")
            if st.button("✨ Generate Caption"):
                with st.spinner("Analyzing image..."):
                    caption = gemini_vision_response(
                        "Describe this image in one natural sentence.",
                        image
                    )
                st.success(caption)


# ================= EMBEDDINGS =================
elif selected == "Text Embeddings":

    st.title("🔡 Text Embedding Generator")

    text = st.text_area(
        "Enter text",
        placeholder="Type text to embed...",
        height=150
    )

    if st.button("⚡ Generate Embedding"):
        if not text.strip():
            st.warning("Please enter some text")
        else:
            with st.spinner("Creating embedding vector..."):
                vector = embeddings_model_response(text)

            dim = len(vector)

            st.success("Embedding generated")

            col1, col2, col3 = st.columns(3)
            col1.metric("Vector Dimension", dim)
            col2.metric("Text Length", len(text))
            col3.metric("Model", "Gemini")

            st.markdown("### 🔍 Vector Preview (first 20 values)")
            st.code(vector[:20])

            with st.expander("📊 Full Embedding Vector"):
                st.write(vector)


# ================= ASK ANYTHING =================
elif selected == "Ask Anything":

    st.title("❓ Ask Gemini Anything")

    question = st.text_area(
        "Your question",
        placeholder="Ask anything..."
    )

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question")
        else:
            with st.spinner("Generating answer..."):
                answer = gemini_text_response(question)

            st.markdown(answer)


# ================= VOICE ASSISTANT =================
elif selected == "Voice Assistant":

    st.title("🎤 Gemini Voice Assistant")

    st.info("Click and speak. Gemini will answer.")

    if st.button("🎙 Start Listening"):
        text = voice_to_text()

        if text:
            st.write("🗣 You said:", text)

            with st.spinner("Gemini thinking..."):
                response = gemini_text_response(text)

            st.success(response)

            # Speak response
            speak(response)
        else:
            st.warning("Could not recognize speech")