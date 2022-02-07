# Jarvis
#this is AI based Voice Assistant by python
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import pywhatkit as kit
import sys
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voices',voices [0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining You!...")
        r.pause_threshold = 3
        audio = r.listen(source,timeout = 1,phrase_time_limit = 5)
    try:
        print("Recognising!!!...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said = {query}")

    except Exception as e:
        speak("Can You Say it Again , speak now")
        return "none"
    query = query.lower()
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>12 and hour < 16:
        speak("Good Afternoon!")

    else:
        speak("Hello there!,Good Evening")
    speak("Namaste! I am Jarvis , Tell Me how Can i help You")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)

if __name__ == '__main__':

    wish()

    while True:

        query = takecommand()
        #performing logical tasks

        if "open notepad" in query:
            path = "%windir%\system32\notepad.exe"
            os.startfile(path)

        elif "what is my mother name" in query:
            speak("Your MOM Name is Neetu Murkute")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "what is my name" in query:
            speak("Pratham Murkute")

        elif "what is date" in query:
            speak(date())

        elif "open camera" in query:
            cap = cv2.VideoCapture(1)
            while True:
                ret.img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "what is your name" in query:
            speak("my name is Jaarvis Tony Stark")

        #C:\Jarvis songs
        elif "play music" in query:
            music_dir = 'C:\Jarvis songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif "open google map" in query:
            webbrowser.open("https://www.google.com/maps")

        elif "play something interesting" in query:
            music_dir = 'C:\Jarvis songs'
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir,song))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "shut up" in query:
            speak("Jii Huzur !")
            break
        elif "open spotify" in query:
            webbrowser.open("https://www.spotify.com")

        elif "open google" in query:
            speak("What should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        # elif "send message" in query:
        #     kit.sendwhatmsg("+9100000000","this is my testing message",2,25)

        elif "play song on youtube" in query:
            kit.playonyt("enemy")

        elif "jarvis tell me a joke" in query:
            speak("J O K E is joke hahahah haha haa")

        elif "goodbye" in query:
            speak("thanks For using me sir , Jai Shree Raam")
            sys.exit()
        elif "play movies" in query:
            speak("onn the wayyy")

        speak("Sir ji , do you have any other Work?")
