import os
import unittest
from pyaudioai.OpenAiResponse import OpenAiResponse

__author__ = "Manuel Eberle (info@manueleberle.de)"

class TestOpenAiResponse(unittest.TestCase):

    openai_obj = OpenAiResponse(os.getenv("OPENAI_API_KEY"))

    def test_init(self):
        assert self.openai_obj.model == "gpt-3.5-turbo"
        assert self.openai_obj.audio_model == "whisper-1"

    def test_transcribe(self):
        print(os.getcwd())
        assert "rechne" in self.openai_obj.transcribe("tests/audio/1plus3.m4a").lower()
    
    def test_transcribe_error(self):
        with self.assertRaises(FileNotFoundError):
            self.openai_obj.transcribe("notavailable.m4a")

    def test_response(self):
        assert "4" in self.openai_obj.get_text_response("tests/audio/1plus3.m4a")


if __name__ == '__main__':
    unittest.main()
