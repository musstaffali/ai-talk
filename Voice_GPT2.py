import openai
import pyttsx3
import speech_recognition as sr
import time

# set your api key
openai.api_key = ""

# initialize the text-to-speech
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()