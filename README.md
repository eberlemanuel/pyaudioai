# PyAudioAI Python Library

![Build and Test](https://github.com/eberlemanuel/pyaudioai/actions/workflows/test.yml/badge.svg)

The Python library combines the OpenAI ChatGPT API with audio input and output. 
With this, questions can be recorded as audio, 
sent to ChatGPT and the answer from ChatGPT can be output as audio again. 
For the audio output, gTTS (Google Text-to-Speech), a Python library and 
CLI tool to interface with Google Translate's text-to-speech API is used.

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install pyaudioai
```

Install from source with:

```sh
python setup.py install
```

## Usage

Portaudio needs to be configured to have access to your computers microphone. 

Linux:
```bash
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
```

Mac OS X:
```bash
brew install portaudio
```

Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

The OpenAI library needs to be configured with your account's secret key **OPENAI_API_KEY** which is available on the [website](https://platform.openai.com/account/api-keys).

Example:

```python
import os
import pyaudioai

audio_file = "question.wav" # question can be saved
question_audio = pyaudioai.RecordQuestion(5, audio_file)
question_audio.record()

response_class = pyaudioai.OpenAiResponse("<OPENAI_API_KEY>")
response_class.get_audio_response(audio_file)

question_audio.delete_file() # delete question audio if required
```

## Developer Documentation

The documentation of the source code for contributors can be found [here](https://eberlemanuel.github.io/pyaudioai/).