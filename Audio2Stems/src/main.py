import os
import streamlit as st
from .demucs_wrapper import separate_audio

def main():
    st.title('Audio Separator | Full Mix To Stems')
    st.write('Separate audio tracks into drums, bass, vocals, and other instruments.')

    audio_file = st.file_uploader("Choose an audio file (.mp3 or .wav)", type=['mp3', 'wav'])
    model_choice = st.selectbox("Select the model for separation:", ['mdx_extra', 'demucs', 'other_model'])

    if st.button('Separate Audio'):
        if audio_file is not None:
            file_path = os.path.join('temp', audio_file.name)
            with open(file_path, "wb") as f:
                f.write(audio_file.getbuffer())
            separate_audio(file_path, model=model_choice)
            st.success(f"Finished separating {audio_file.name}")
        else:
            st.error("Please upload an audio file.")

if __name__ == "__main__":
    main()
