# voice_synthesizer.py
from TTS.api import TTS

class VoiceSynthesizer:
    def __init__(self, model_name="tts_models/en/ljspeech/tacotron2-DDC"):
        self.tts = TTS(model_name=model_name)

    def synthesize_voice(self, text: str, output_path: str):
        self.tts.tts_to_file(text=text, file_path=output_path)
