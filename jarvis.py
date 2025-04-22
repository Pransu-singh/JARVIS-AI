import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import pywhatkit as wk
import urllib.parse
import ctypes
import threading
import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
from PIL import Image, ImageTk

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
    
    speak("what can i do for you ")
    
    
def takeCommand():
    
       r = sr.Recognizer()
       with sr.Microphone() as source:
            update_gui ("Listening....")
            r.pause_threshold=1
            audio = r.listen(source) 


       try:
            update_gui ("recognizing....")
            query = r.recognize_google(audio,language='en-in')
            update_gui(f"User said: {query} \n")      


       except Exception as e:
            update_gui("Say that again please....")
            return "None"
       return query

def run_jarvis():
    global running
    running = True
    WishMe()
    
    while running:
        query = takeCommand().lower()  # Listen for voice commands
        process_command(query)  # Process the command




def process_command(query):
        if not query or query =="none":
          return 
     
        if 'jarvis' in query:
            
            update_gui("yes sir")
            speak("yes sir")

        elif "who are you" in query  or "hu r u" in query:
            update_gui('My Name Is Jarvis ')
            speak("My Name Is Jarvis")
            update_gui("I can do everything that my creator programmed me to do")
            speak("I can do everything that my creator programmed me to do")
        elif "who created you" in query:
            update_gui("I am created by Mr. Pransu Singh , i created with python language, in visual studio code")
            speak("I am created by Mr. Pransu Singh , i created with python language, in visual studio code")
        

        elif 'what is ' in query:
           speak('Searching Wikipedia...')
           query = query.replace("what is ", "")

           try:
             results = wikipedia.summary(query, sentences=2)
             speak("According to Wikipedia:")
             update_gui(results)
             speak(results)
           except wikipedia.exceptions.DisambiguationError as e:
             update_gui("The query is too broad. Please be more specific.")
             speak("The query is too broad. Please be more specific.")
           except wikipedia.exceptions.PageError:
             update_gui("No results found on Wikipedia.")
             speak("No results found on Wikipedia.")
           except Exception as e:
             update_gui("An error occurred while searching.")
             speak("An error occurred while searching.")

        elif 'who is ' in query:
          speak('Searching Wikipedia...')
          query = query.replace("who is ", "")

          try:
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia:")
              update_gui(results)
              speak(results)
          except wikipedia.exceptions.DisambiguationError as e:
             update_gui("The query is too broad. Please be more specific.")
             speak("The query is too broad. Please be more specific.")
          except wikipedia.exceptions.PageError:
            update_gui("No results found on Wikipedia.")
            speak("No results found on Wikipedia.")
          except Exception as e:
             update_gui("An error occurred while searching.")
             speak("An error occurred while searching.")

            
        elif 'open google' in query:
            speak("What should I search on Google?")
            qry = takeCommand().lower()

            if qry:  
               url = f"https://www.google.com/search?q={qry}"
               webbrowser.open(url)
               speak(f"Searching Google for {qry}")
            else:
               webbrowser.open("https://www.google.com")
               speak("Opening Google")

            
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
        
        elif "close edge" in query or "close browser" in query:  
            speak("Closing Microsoft Edge")  
            os.system("taskkill /f /im msedge.exe")

        
        elif "close chrome" in query:  
            speak("Closing Google Chrome")  
            os.system("taskkill /f /im chrome.exe")
 
                                   
         ###################################################
        elif "open paint" in query: 
             speak("Opening Paint")
             os.startfile("mspaint.exe")
        
        elif "close paint" in query:  
           speak("Closing Paint")  
           os.system("taskkill /f /im mspaint.exe")

        elif "open notepad" in query:  
             speak("Opening Notepad")  
             os.startfile("notepad.exe")  

        elif "close notepad" in query:  
           speak("Closing Notepad")  
           os.system("taskkill /f /im notepad.exe")
        
        
        elif "open command prompt" in query:  
           speak("Opening Command Prompt")  
           os.system("start cmd")  

        elif "close command prompt" in query:  
           speak("Closing Command Prompt")  
           os.system("taskkill /f /im cmd.exe")
        elif "write in notepad" in query:
          speak("Opening Notepad")
          os.system("notepad.exe")  # Opens Notepad
          time.sleep(2)  # Wait for Notepad to open

          speak("What should I write?")
          while True:
               text = takeCommand()
               if "exit" in text.lower():
                 speak("Stopping writing.")
                 break  # Stops writing
               elif "clear" in text.lower():
                  pyautogui.hotkey("ctrl", "a")  # Select all text
                  pyautogui.press("backspace")  # Delete selected text
                  speak("Notepad cleared. Start writing again.")
               else:
                  pyautogui.typewrite(text + "\n", interval=0.1)  # Types in Notepad


         
         
         
        
        elif 'tell me the time' in query: #23
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"sir time is {strTime}")
        

        elif "shut down the system" in query:
           speak("Shutting down your system in 5 seconds.")
           os.system("shutdown /s /t 5")  # Shuts down after 5 seconds

        elif "restart the system" in query:
           speak("Restarting your system in 5 seconds.")
           os.system("shutdown /r /t 5")  # Restarts after 5 seconds

        elif "sleep the system" in query or "hibernate the system" in query:
          speak("Putting the system to sleep.")
          os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Sleep or Hibernate

        elif "lock the system" in query:
          speak("Locking the system.")
          os.system("rundll32.exe user32.dll,LockWorkStation")  # Locks the system

        elif "switch user" in query:
          speak("Switching user.")
          ctypes.windll.user32.LockWorkStation() 
 
         

        elif "open vscode" in query or "open visual studio code" in query:
           speak("Opening Visual Studio Code.")
           os.system("code")  # Works if VS Code is added to system PATH

         
        elif "close vscode" in query or "close visual studio code" in query:
            speak("Closing Visual Studio Code.")
            os.system("taskkill /f /im Code.exe")  # Forcefully closes VS Code

         
            
         
        
        
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
                  speak("Ready")
                  update_gui("Listening...")
                  r.adjust_for_ambient_noise(source)
                  audio = r.listen(source)
    
                try:
                    my_string = r.recognize_google(audio).lower()
                    update_gui(f"Recognized: {my_string}")

                    def get_operator_fn(op):
                      return {
                          "+": operator.add, "plus": operator.add,
                          "-": operator.sub, "minus": operator.sub,
                          "x": operator.mul, "times": operator.mul,
                          "/": operator.truediv, "divided": operator.truediv
                        }.get(op, None)

                    def eval_binary_expr(op1, oper, op2):
                       return get_operator_fn(oper)(int(op1), int(op2)) if get_operator_fn(oper) else "Invalid Operator"

                    words = my_string.split()
                    if len(words) == 3:
                       result = eval_binary_expr(*words)
                       speak(f"Your result is {result}")
                       update_gui(f"Result: {result}")
                    else:
                          speak("Invalid input format. Please say numbers and an operator.")

                except sr.UnknownValueError:
                   speak("Sorry, I could not understand")
                except sr.RequestError:
                      speak("Speech recognition service is unavailable")
                except Exception as e:
                    speak("An error occurred while calculating")
                    update_gui(f"Error: {e}")

        elif "click photo" in query or "take a picture" in query:  
            speak("Getting ready to take a photo")  
            cap = cv2.VideoCapture(0)  # Open the webcam  

            ret, frame = cap.read()  # Capture a frame  
            if ret:
              filename = "captured_photo.jpg"
              cv2.imwrite(filename, frame)  # Save the image  
              speak("Photo captured successfully")
              update_gui(f"Photo saved as {filename}")
            else:
               speak("Failed to capture photo")

            cap.release()  # Release the webcam  
            cv2.destroyAllWindows()  # Close any OpenCV windows
        
        
        elif "show photo" in query:  
            filename = "captured_photo.jpg"

            if os.path.exists(filename):  
               speak("Displaying the captured photo")  

        # Read image
               img = cv2.imread(filename)  
        
               if img is None:
                 speak("Failed to load the photo.")
                 update_gui("Failed to load the photo.")
               else:
            # Show image in a non-blocking way
                  cv2.imshow("Captured Photo", img)  
                  cv2.waitKey(5000)  # Show for 2 seconds (2000 milliseconds)
                  cv2.destroyAllWindows()  

            else:  
               speak("No photo found. Please take a picture first.")  


        elif "open whatsapp" in query:
             speak("Opening WhatsApp")
             os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")

         
         

        elif "send whatsapp message" in query:
           speak("To whom should I send the message?")
           contact = takeCommand().lower()

    # Define contacts (Add your contacts here)
           contacts = {
            "pranshu bhai": "pranshu bhai ",
              "vipin ritik": "vipin ritik"
           }

           if contact in contacts:
             speak("What is the message?")
             message = takeCommand()

        # Open WhatsApp Desktop
             os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
             time.sleep(7)  # Wait for WhatsApp to open

        # Click on the search bar (Adjust coordinates if necessary)
             pyautogui.click(x=211, y=149)  # Adjust for your screen resolution
             time.sleep(1)

        # Type contact name
             pyautogui.write(contacts[contact])
             time.sleep(2)
             pyautogui.press("down")  # Moves to the first result in the list
             time.sleep(1)
             pyautogui.press("enter")
             time.sleep(2)

        # Type message 
             pyautogui.click(x=806, y=991)  # **UPDATE: Find the correct position using pyautogui.position()**
             time.sleep(1)
             pyautogui.write(message)
             time.sleep(1)

        # Send message
             pyautogui.press("enter")
             speak(f"Message sent to {contact}")

           else:
            speak("I don't have this contact saved. Please provide a valid name.")
        
        
        elif "close whatsapp" in query:
               speak("Closing WhatsApp")
               os.system("taskkill /f /im WhatsApp.exe")  # Forcefully closes WhatsApp

def update_gui(text):
    response_label.configure(text=text)  # Update response label in GUI


# Function to start Jarvis in a separate thread
def start_jarvis():
    global running
    running = True
    threading.Thread(target=run_jarvis, daemon=True).start()
 
 
def handle_text_command():
    global running
    command = text_command_entry.get().strip().lower()  # Get user input
    text_command_entry.delete(0, 'end')  # Clear the entry box after submission
    
    if command:
        update_gui(f"User typed: {command}")  # Show user input in GUI
        process_command(command)  # Process the command
 

# Function to stop Jarvis
def stop_jarvis():
    global running
    running = False
    update_gui("Jarvis is shutting down.")
    speak("Jarvis is shutting down.")
    tk_root.quit()

 

# Initialize the UI
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Default theme

tk_root = ctk.CTk()  # Create main window
tk_root.title("Jarvis AI Assistant")
tk_root.geometry("600x500")

# UI Title
title_label = ctk.CTkLabel(tk_root, text="Jarvis AI Assistant", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Display area for responses
response_label = ctk.CTkLabel(tk_root, text="Welcome! Click 'Start' to begin.", font=("Arial", 14), wraplength=500)
response_label.pack(pady=20)


# Input field for text commands
text_command_entry = ctk.CTkEntry(tk_root, width=400, font=("Arial", 14))
text_command_entry.pack(pady=10)

# Button to submit text command
submit_button = ctk.CTkButton(tk_root, text="Submit Command", command=lambda: handle_text_command())
submit_button.pack(pady=10)



# Start & Stop buttons
start_button = ctk.CTkButton(tk_root, text="Start Listening", command=lambda: threading.Thread(target=run_jarvis, daemon=True).start())
start_button.pack(pady=10)

stop_button = ctk.CTkButton(tk_root, text="Exit", command=tk_root.quit, fg_color="red")
stop_button.pack(pady=10)

# Run the GUI
tk_root.mainloop()
