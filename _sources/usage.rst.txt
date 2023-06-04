Usage
==========

Portaudio needs to be configured to have access to your computers microphone. 

**Linux:**

.. code-block:: python

  sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

**Mac OS X:**

.. code-block:: python

  brew install portaudio


**Windows:**

.. code-block:: python

  pip install pipwin
  pipwin install pyaudio


The OpenAI library needs to be configured with your account's secret key **OPENAI_API_KEY** which is available on the [website](https://platform.openai.com/account/api-keys).

**Example:**

.. code-block:: python

  import os
  import pyaudioai  

  audio_file = "question.wav" # question can be saved
  question_audio = pyaudioai.RecordQuestion(5, audio_file)
  question_audio.record()  

  response_class = pyaudioai.OpenAiResponse("<OPENAI_API_KEY>")
  response_class.get_audio_response(audio_file)  

  question_audio.delete_file() # delete question audio if required
