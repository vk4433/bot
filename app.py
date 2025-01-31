import streamlit as st
import speech_recognition as spr
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv()
google_api_key = os.getenv("google_api")
genai.configure(api_key=google_api_key)

st.set_page_config(page_title="Talk & Translate 🗣️✨", page_icon="🗣️", layout="centered")

recognizer = spr.Recognizer()
mic = spr.Microphone()

def recognize_speech(recog, source):
    try:
        recog.adjust_for_ambient_noise(source, duration=0.05)
        audio = recog.listen(source)
        recognize_text = recog.recognize_google(audio)
        return recognize_text
    except spr.UnknownValueError:
        st.error("Cannot detect the audio")
        return None
    except spr.RequestError as exe:
        st.error(f"Error in recognition: {exe}")
        return None

language_map = {
    'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Kannada': 'kn', 'Tamil': 'ta',
    'Malayalam': 'ml', 'Bengali': 'bn', 'German': 'de', 'Chinese': 'zh-CN',
    'Japanese': 'ja', 'Arabic': 'ar', 'Italian': 'it', 'Korean': 'ko'
}

st.markdown("""
# Talk & Translate 🗣️🔁
Speak in any language 🌍, generate content ✍️, translate it 🔄, and hear the audio translation 🎧 in your chosen language. Select languages and start recording 🎙️!
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox("Select the source language:", list(language_map.keys()), index=0)
with col2:
    target_language = st.selectbox("Select the target language:", list(language_map.keys()), index=0)

source = language_map[source_language]
target = language_map[target_language]

# Translate Speech
if st.button("Translate Speech 🎙️", use_container_width=True):
    st.write("🎙️ Started recording... Speak now!")
    
    with st.spinner("Listening..."):
        with mic as source_audio:
            my_text = recognize_speech(recognizer, source_audio)

    if my_text:
        st.success(f"Recognized Text: {my_text}")
        try:
            detect_language = detect(my_text)
            st.write(f"Detected Language: {detect_language}")
            
            if not os.path.exists('outputs'):
                os.makedirs('outputs')

            # Translate text to target language
            translated_text = GoogleTranslator(source=detect_language, target=target).translate(my_text)
            st.write(f"Translated Text in {target_language}: {translated_text}")

            # Convert translated text to speech
            speak = gTTS(text=translated_text, lang=target, slow=False)
            audio_file = f"outputs/captured_voice_{target}.mp3"
            speak.save(audio_file)
            st.audio(audio_file, format="audio/mp3")
        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
    else:
        st.warning("No speech detected. Please try again!")

# Explain Topic
if st.button("Search Topic🌍", use_container_width=True):
    st.write("🎙️ Started recording... Speak now!")
    
    with st.spinner("Listening..."):
        with mic as source_audio:
            topic = recognize_speech(recognizer, source_audio)

    if topic:
        try:
            with st.spinner("Fetching explanation and generating audio..."):
                # Generate content using Google's generative AI model (Gemini)
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(topic)
                explanation_text = response.text.strip()
                
                if not explanation_text:
                    st.error("Failed to generate an explanation. Please try again with a different topic.")
                else:
                    detect_language = detect(explanation_text)
                    translated_explanation = GoogleTranslator(source=detect_language, target=target).translate(explanation_text)
                    st.write("### Explanation:")
                    st.write(f"Translated explanation in {target_language}: {translated_explanation}")
                    
                    # Convert explanation to speech
                    speak = gTTS(text=translated_explanation, lang=target, slow=False)
                    audio_file = f"outputs/explanation_{target}.mp3"
                    speak.save(audio_file)
                    st.audio(audio_file, format="audio/mp3")
        except Exception as e:
            st.error(f"An error occurred during explanation generation: {e}")
    else:
        st.warning("Please enter a topic before clicking 'Explain Topic'!")
