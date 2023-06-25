from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from pyjokes import pyjokes
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import wolframalpha
import speedtest



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Yes Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Yes Sir") 
    else:
        speak("Good Evening! Yes Sir")
 
speak("Ready To Comply. My name is Friday. What can I do for you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...")
        speak("Say that again please...")
        return "None"

    return query



def TaskExecution():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "channel analytics" in query:
            webbrowser.open("https://studio.youtube.com/channel/UCxeYbp9rU_HuIwVcuHvK0pw/analytics/tab-overview/period-default")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")

        

       
            
        

        



if __name__ == "__main__":
    while True:
        permission=takeCommand().lower()
        if "friday" in permission:
            TaskExecution()

        elif "goodbye friday" in permission:
            sys.exit()

        