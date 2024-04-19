from demucs_wrapper import separate_audio

def separate_audio(audio_file, model='mdx_extra'):
    """
    Separates the audio file using the Demucs model.
    """
    demucs.separate.main(["--mp3", "-n", model, audio_file])
