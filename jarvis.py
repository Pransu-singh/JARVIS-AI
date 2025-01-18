import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import pywhatkit as wk
import os
import random
import cv2
import time
import operator
import requests
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning!")
    elif hour >=12 and hour <18 :
        speak("good afternoon")
    else :
        speak("good evening !")
    
    speak("Ready to comply. what can i do for you ?")
    
    
def takeCommand():
    
       r = sr.Recognizer()
       with sr.Microphone() as source:
           print("Listening....")
           r.pause_threshold=1
           audio = r.listen(source) 


       try:
            print ("recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query} \n")      


       except Exception as e:
            print("Say that again please....")
            return "None"
       return query

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            
            print("yes sir")
            speak("yes sir")

        elif "who are you" in query:
            print('My Name Is Jarvis ')
            speak('My Name Is Jarvis')
            print("I can do everything that my creator programmed me to do")
            speak("I can do everything that my creator programmed me to do")
        elif "who created you" in query:
            print("I am created by Mr. Pransu Singh , i created with python language, in visual studio code ")
            speak('I am created by Mr. Pransu Singh , i created with python language, in visual studio code')
        elif 'what is ' in query:
            speak ('searching wikipedia.....')
            query = query.replace("what is ", "")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)
        
        elif 'who is' in query:
            speak ('searching wikipedia.....')
            query = query.replace("who is ", "")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)
            
        elif 'open google' in query:
            speak("what should i search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry,sentences=1)
            speak(results)
            
        elif 'just open Google' in query:
            webbrowser.open('www.google.com')
        
        elif 'type' in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}",0.1)
        
        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open youtube' in query:
            speak("what will you like to watch ?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")
            
        elif 'search on youtube' in query:
            query = query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        
        elif 'close browser ' in query:
            os.system("taskkill /f /im msedge.exe")
        
        elif 'close chrome 'in query:
            os.system("taskkill /f /im chrome.exe") 
                                   
         ###################################################
        # elif "open paint" in query: 
        #     npath = "C:\WINDOWS\system32\\mspaint.exe" 
        #     os.startfile("npath")
        # elif "close paint" in query: 
        #     os.system("taskkill /f /im mspaint.exe")
        # elif "open notepad" in query: 
        #     npath = "C:\WINDOWS\system32\\notepad.exe" 
        #     os.startfile(npath)
        # elif "close notepad" in query:  
        #     os.system("taskkill /f /im notepad.exe")
        # elif "open command prompt" in query: 
        #     os.system("start cmd")
        # elif "close command prompt" in query: 
        #     os.system("taskkill /f /im cmd.exe")
        # elif 'play music' in query: #19 
        #     music_dir = 'E:\Musics'
        #     songs = os.listdir (music_dir)
        #     os.startfile(os.path.join(music_dir, random.choice(songs)))
         
        # elif 'close music' in query: #22
        #     os.system("taskkill /f /im vlc.exe")
        elif 'tell me the time' in query: #23
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"sir time is {strTime}")
            
        # elif "shut down the system" in query:
        #     os.system("shutdown /s /t 5")
        
        # elif "restart the system" in query:
        #     os.system("restart /s /t 5")
        
        # elif "lock the system " in query:
        #     os.system("rundll32.exe powrprof.dll,setsuspendstate 0,1,0")
        
        # elif "hibernate the system " in query:
        #     os.system("rundll32.exe powrprof.dll,setsuspendstate 0,1,0")
        
        
        elif "open camera" in query:
            cap= cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        
        elif "go to sleep" in query:
            speak('alright then, i am switching off')
            sys.exit()
        
        elif "take screenshot" in query:
            speak('tell me a name of a file') 
            name=takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")
        
        elif "calculate" in query: 
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided' : operator.__truediv__,
                }[op]   
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        # elif "what is my in address" in query: