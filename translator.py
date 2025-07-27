import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import streamlit.components.v1 as components
#from streamlit_extras.copy_to_clipboard import copy_to_clipboard
import os
import tempfile


translator = Translator()

st.set_page_config(page_title="CodeAlpha", page_icon="🌍")
st.title("Language Translation Tool  ")
#input TExt
text_to_translate = st.text_area("Enter text")

#Language selection
lang_list = list(LANGUAGES.values())
target_lang_name = st.selectbox("Select Target Language :", lang_list)

lang_code= [code for code , name in LANGUAGES.items() if name==target_lang_name][0]


# Translate and process
if st.button(" Translate"):
    if text_to_translate.strip():
        translated = translator.translate(text_to_translate, dest=lang_code)
        st.subheader(" Translated Text:")
        st.success(translated.text)

        # Copy to clipboard
        #copy_to_clipboard(translated.text)

        # Text-to-Speech using gTTS
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts = gTTS(text=translated.text, lang=lang_code)
                tts.save(fp.name)
                audio_file = open(fp.name, "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.error("Text-to-speech failed. Language might not be supported.")
    else:
        st.warning("Please enter some text to translate.")
