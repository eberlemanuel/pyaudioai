import os
import openai
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

__author__ = "Manuel Eberle (info@manueleberle.de)"

class OpenAiResponse:
    """
    A class used to get a text or an audi response from OpenAI ChatGPT.

    Attributes
    ----------
    api_key : str
        key to authenticate through OpenAI API https://platform.openai.com/account/api-keys
    model : str
        select a ChatGPT model https://platform.openai.com/docs/guides/gpt (default gpt-3.5-turbo)
    audio_model : str
        select a speech to text model https://platform.openai.com/docs/guides/speech-to-text (default whisper-1)
    """

    def __init__(self, api_key, model = "gpt-3.5-turbo", audio_model = "whisper-1"):
        """
        Parameters
        ----------
        api_key : str
            key to authenticate through OpenAI API https://platform.openai.com/account/api-keys
        model : str
            select a ChatGPT model https://platform.openai.com/docs/guides/gpt (default gpt-3.5-turbo)
        audio_model : str
            select a speech to text model https://platform.openai.com/docs/guides/speech-to-text (default whisper-1)
        """

        openai.api_key = api_key
        self.model = model
        self.audio_model = audio_model

    def transcribe(self, audio_file):
        """Transcribe an audio file to text.

        Parameters
        ----------
        audio_file : str, required
            Path to an audio file which contains a question

        Raises
        ------
        FileNotFoundError
            If the audio file is not found
        """

        if not os.path.exists(audio_file):
            raise FileNotFoundError("[ERROR] file '{}' not found".format(audio_file))
        
        audio_stream = open(audio_file, "rb")
        transcript = openai.Audio.transcribe(self.audio_model, audio_stream)
        return transcript.text

    def get_text_response(self, audio_file):
        """Get a text response of an audio file which contains a question.

        Parameters
        ----------
        audio_file : str, required
            Path to an audio file which contains a question
        
        Returns
        -------
        str
            response from ChatGPT as text
        """

        response = openai.ChatCompletion.create(
        model = self.model,
        messages = [
                {"role": "system", "content": self.transcribe(audio_file)}
            ]
        )
        return response.choices[0].message.content
    
    def get_audio_response(self, audio_file):
        """Get an audio response of an audio file which contains a question.
        The function converts the text repsonse with TTS to an audio object
        and plays the audio.

        Parameters
        ----------
        audio_file : str, required
            Path to an audio file which contains a questio
        """
        text_response = self.get_text_response(audio_file)
        print("[INFO] {}".format(text_response))
        
        gTTS(text=text_response, lang='de').write_to_fp(voice := NamedTemporaryFile())
        playsound(voice.name)
        voice.close()