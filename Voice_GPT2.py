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
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognizer_google(audio)
    except:
        print('Skipping unknown error')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000.
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["rext"]