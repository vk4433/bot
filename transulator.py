import streamlit as st
import speech_recognition as spr
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
google_api_key = os.getenv("google_api")

st.set_page_config(page_title="Talk & Translate 🗣️✨", page_icon="🗣️", layout="centered")

recognizer = spr.Recognizer()
mic = spr.Microphone()

def recognize_speech (recog,source):
    try:
        recog.adjust_for_ambient_noise(source,duration=0.5)
        audio = recog.listen(source)
        recognize_text = recog.recognize_google(audio)
        return recognize_text
    except spr.UnknownValueError:
        st.error("canot detect the audio")
        return None
    except spr.RequestError as exe:
        st.error(f"error in recognization:{exe}")
        return None
    
# Language mapping
language_map = {
    'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Kannada': 'kn', 'Tamil': 'ta',
    'Malayalam': 'ml', 'Bengali': 'bn', 'German': 'de', 'Chinese': 'zh-CN',
    'Japanese': 'ja', 'Arabic': 'ar', 'Italian': 'it', 'Korean': 'ko'
}

# Streamlit UI (Centered content)
st.title("Talk & Translate 🗣️🔁")
st.markdown("""
This application captures your speech, detects the language, translates it, and then converts it back to speech in the target language. 
Choose the source and target language, then click the "Start Speaking" button to begin.
""", unsafe_allow_html=True)

col1,col2= st.columns([1,1])

with col1:
    source_language = st.selectbox("Select the source language:", list(language_map.keys()), index=0)
with col2:
    target_language = st.selectbox("Select the target language:", list(language_map.keys()), index=0)
 

source = language_map[source_language]
target = language_map[target_language]

if st.button("Start Speaking",use_container_width=True):
    with st.spinner("say anything to transulate"):
        with mic as source:
            my_text = recognize_speech(recognizer,source)
    if my_text:
        st.success(f"recognized_text{my_text}")
        try:
            detect_language = detect(my_text)
            st.write(f"Detected Language: {detect_language}")

            if not os.path.exists('outputs'):
              os.makedirs('outputs')
            # Translate the recognized text
            translated_text = GoogleTranslator(source=detect_language, target=target).translate(my_text)
            st.write(f"Translated Text in {target}: {translated_text}")

            speak = gTTS(text=translated_text, lang=target, slow=False)
            audio_file = f"outputs/captured_voice_{target}.mp3"
            speak.save(audio_file)

            st.audio(audio_file, format="audio/mp3")

        except Exception as e:
            st.error(f"An error occurred during translation: {e}")

    else:
        st.warning("No speech detected. Please try again!")

else:
    st.info("Click the button to start the voice recognition and translation process.")


