import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
# Record Audio
r = sr.Recognizer()
record_time = time.time()
while True:
    with sr.Microphone() as source: # open the microphone and start recording
        audio = r.listen(source)
        print("Say something!")

    # Speech recognition using Google Speech Recognition
    try:
        current_time = time.time()
        if current_time - record_time >= 10: # if recording time more than 10s, quit.
            print(current_time - record_time)
            break
        print("You said: " + r.recognize_google(audio))
        record_time = time.time()
    except sr.UnknownValueError:  # exception if the speech is unintelligible
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
