import os
os.environ["PATH"] += os.pathsep + "/usr/bin/ffmpeg" 
import speech_recognition as sr
from io import BytesIO
from gtts import gTTS
import subprocess
import logging
# import warnings

class Converter:
    def __init__(self, file_bytes):
        self.ogg = 'audio.ogg'
        self.wav = 'audio.wav'
        self.file_bytes = file_bytes
        self.recognizer = sr.Recognizer()
        logging.disable(logging.CRITICAL)    

    # audio to text
    def convert_to_wav(self):
        # print('hello conv')
        try:
            subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'panic', '-i', self.ogg, '-acodec', 'pcm_s16le', '-ar', '16000', self.wav])
        except:
            pass 

    def audio_to_text(self):  
        # logging.disable(logging.INFO) 
        recognized_text = None         
        
        try:
            with sr.AudioFile(self.wav) as source:
                audio = self.recognizer.record(source)
            # with warnings.catch_warnings():
            #     warnings.simplefilter("ignore")
            recognized_text = self.recognizer.recognize_google(audio, language='ru-RU')
        except:
            pass
        
        try:
            self.delete_audio_files()
        except:
            pass

        return recognized_text

    def delete_audio_files(self):
        for file in os.listdir('.'):
            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
                os.remove(file)
     
    def main_convertor_to_text(self):
        recognized_text = None
        try:
            with open(self.ogg, 'wb') as audio_file:
                audio_file.write(self.file_bytes.getvalue())
        except:
            pass
        try:
            self.convert_to_wav()
        except:
            pass
        try:
            recognized_text = self.audio_to_text()
        except:
            pass
        return recognized_text 
    # audio to text end    
    
    # text to audio
    def convert_text_to_audio(self, text):
        try:
            # print('two')
            audio_path = 'audio.mp3'
            tts = gTTS(text=text, lang='ru')        
            tts.save(audio_path)
            # print('three')
            return True
        except:
            return False

      


