# NOTE: python -m speech_recognition as command

import pyttsx3
import webbrowser
import speech_recognition as sr

# preferences = {"Kipsy": [6, "Playing In-A-Gadda-Da-Vida and displaying weather.", [inagaddadavida(), weather()]]}

def audio_file_to_text():
    r = sr.Recognizer()
    harvard = sr.AudioFile('harvard.wav')
    with harvard as source:
        audio = r.record(source)
    print(r.recognize_google(audio))

def text_to_speech(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[6].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-75)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    engine.say(text)
    engine.runAndWait()

def weather():
    webbrowser.open('https://weather.com/')

def inagaddadavida():
    webbrowser.open('https://www.youtube.com/watch?v=UIVe-rZBcm4')

def main(name):
    text_to_speech("Welcome, " + name + "!")
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            text_to_speech("What can I do for you?")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_to_speech("You said " + text)
            if "bye" in text:
                text_to_speech("Goodbye, " + name + "! Shutting down.")
                break
            if "weather" in text:
                weather()
                text_to_speech("Here's the weather.")
            if "In-A-Gadda-Da-Vida" in text or "inagodadavida" in text:
                inagaddadavida()
                text_to_speech("Playing Professor Rowland's favorite song.")
            if "hello" in text or "hi" in text:
                text_to_speech("Hello! Nice to see you again.")

        except sr.UnknownValueError:
            text_to_speech("I could not understand you.")

main("Kipsy")

#speaker identification
#different voices DONE
#cartoon animation speaking