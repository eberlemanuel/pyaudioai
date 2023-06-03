import os
import openai
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

class OpenAiResponse:

    def __init__(self, api_key, model = "gpt-3.5-turbo", audio_model = "whisper-1"):
        openai.api_key = api_key
        self.model = model
        self.audio_model = audio_model

    def transcribe(self, audio_file):
        if not os.path.exists(audio_file):
            raise FileNotFoundError("[ERROR] file '{}' not found".format(audio_file))
        
        audio_stream = open(audio_file, "rb")
        transcript = openai.Audio.transcribe(self.audio_model, audio_stream)
        return transcript.text

    def get_text_response(self, audio_file):
        response = openai.ChatCompletion.create(
        model = self.model,
        messages = [
                {"role": "system", "content": self.transcribe(audio_file)}
            ]
        )
        return response.choices[0].message.content
    
    def get_audio_response(self, audio_file):
        text_response = self.get_text_response(audio_file)
        print("[INFO] {}".format(text_response))
        
        gTTS(text=text_response, lang='de').write_to_fp(voice := NamedTemporaryFile())
        playsound(voice.name)
        voice.close()