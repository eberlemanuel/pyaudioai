import os
import wave
import pyaudio

class RecordQuestion:

    __format = pyaudio.paInt16
    __channel = 2
    __rate = 44100
    __chunk = 1024

    def __init__(self, recording_time, audio_file):
        self.recording_time = recording_time
        self.audio_file = audio_file

    def record(self):
        pyaudio_obj = pyaudio.PyAudio()
        audio_stream = pyaudio_obj.open(format=self.__format, channels=self.__channel, rate=self.__rate, input=True, frames_per_buffer=self.__chunk)
        
        print("[INFO] Start recording!")
        audio_frames = []
        for _ in range(0, int(self.__rate / self.__chunk * self.recording_time)):
            data_stream = audio_stream.read(self.__chunk)
            audio_frames.append(data_stream)
        
        audio_stream.stop_stream()
        audio_stream.close()
        pyaudio_obj.terminate()
        print("[INFO] Stop recording!")
        
        audio_output = wave.open(self.audio_file, 'wb')
        audio_output.setnchannels(self.__channel)
        audio_output.setsampwidth(pyaudio_obj.get_sample_size(self.__format))
        audio_output.setframerate(self.__rate)
        audio_output.writeframes(b''.join(audio_frames))
        audio_output.close()

    def delete_file(self):
        os.remove(self.audio_file)