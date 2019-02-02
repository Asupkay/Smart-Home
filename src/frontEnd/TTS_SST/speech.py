# NOTE: python -m speech_recognition as command

import pyttsx3
import webbrowser
import speech_recognition as sr
import os
# NEXT LINE NOT IN USE ANYMORE
# from winreg import HKEY_CURRENT_USER, OpenKey, QueryValue
import time

flag = 0
count = 0

# NEXT 3 LINES NOT IN USE ANYMORE
# def get_default_browser():
#     with OpenKey(HKEY_CURRENT_USER, r"Software\Classes\http\shell\open\command") as key:
#         return QueryValue(key, None)

def greet_user(final_name, conf):
    if conf >= .9:
        text_to_speech("Welcome, " + final_name + "!")
        return final_name
    elif conf < .9 and conf >= .7:
        final_name = check_name(final_name)
        return final_name
    elif conf < .7:
        text_to_speech("I could not recognize you through the camera!")
        final_name = check_name("Unknown")
        return final_name

def check_name(name):
    global count
    if name == "Unknown":
        name = new_name()
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            text_to_speech(name + ", is that you?")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                text_to_speech("You said " + text)
                if "yes" in text or "yea" in text or "yup" in text:
                    final_name = name
                    text_to_speech("At last! Welcome, " + final_name + "!")
                    return final_name
                else:
                    # text_to_speech("I must have gotten you confused!")
                    count += 1
                    if count >= 3:
                        final_name = "Guest"
                        text_to_speech("I'm sick of all this back and forth. Please ask the homeowner to add you as a new user.")
                        text_to_speech("Welcome, " + final_name + "!")
                        return final_name
                    else:
                        name = new_name()
            except sr.UnknownValueError:
                text_to_speech("I could not understand you.")

def new_name():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            text_to_speech("What is your first name?")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                text_to_speech("You said " + text)
                final_name = text
                return final_name
            except sr.UnknownValueError:
                text_to_speech("I could not understand you.")

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
    global flag
    if flag == 0:
        webbrowser.get('firefox').open('https://weather.com/weather/today/l/USNJ0221:1:US')
    else:
        webbrowser.get('firefox').open_new_tab('https://weather.com/weather/today/l/USNJ0221:1:US')
    flag += 1

def inagaddadavida():
    global flag
    if flag == 0:
        webbrowser.get('firefox').open('https://www.youtube.com/watch?v=UIVe-rZBcm4')
    else:
        webbrowser.get('firefox').open_new_tab('https://www.youtube.com/watch?v=UIVe-rZBcm4')
    flag += 1

def netflix():
    global flag
    if flag == 0:
        webbrowser.get('firefox').open("https://www.netflix.com/watch/80080569?trackId=14170056&tctx=1%2C1%2C067b8cb5-8757-4638-a78f-7a6788dbd38e-106751798%2C670d5369-7ebb-4c22-9fd3-f6b9194d2187_8585115X10XX1543276222186%2C670d5369-7ebb-4c22-9fd3-f6b9194d2187_ROOT")
    else:
        webbrowser.get('firefox').open_new_tab("https://www.netflix.com/watch/80080569?trackId=14170056&tctx=1%2C1%2C067b8cb5-8757-4638-a78f-7a6788dbd38e-106751798%2C670d5369-7ebb-4c22-9fd3-f6b9194d2187_8585115X10XX1543276222186%2C670d5369-7ebb-4c22-9fd3-f6b9194d2187_ROOT")
    flag += 1

def main(user_list):
    name = user_list[0]
    conf = user_list[1]
    text_to_speech("Evee starting up...")
    print("Please pause for 2 seconds every time before speaking to me. I'm still learning the human language!")
    time.sleep(4)
    final_name = name.split('_', 1)[0]
    final_name = greet_user(final_name, conf)
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            text_to_speech("What can I do for you?")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_to_speech("You said " + text)
            if "bye" in text:
                text_to_speech("Goodbye, " + final_name + "! Shutting down.")
                # if default == "\"C:\Program Files (x86)\Mozilla Firefox\firefox.exe\" -osint -url \"%1\"":
                    # print("good")
                os.system('pkill -f firefox')
                break
            if "weather" in text:
                weather()
                text_to_speech("Here's the weather.")
            if "In-A-Gadda-Da-Vida" in text or "inagodadavida" in text or "In A Gadda Da Vida" in text:
                inagaddadavida()
                text_to_speech("Playing Professor Rowland's favorite song.")
            if "hello" in text or "hi" in text:
                text_to_speech("Hello! Nice to see you again.")
            if "netflix" in text or "Netflix" in text:
                netflix()
                text_to_speech("Playing most recently watched show.")

        except sr.UnknownValueError:
            text_to_speech("I could not understand you.")

main(["Kipsy_Quevada", .95])