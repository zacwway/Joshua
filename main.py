import datetime
from web_search import Web_Search
import pyttsx3
import speech_recognition
import os
import random

START_MENU = r"C:\\Users\\zacwa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\"

engine = pyttsx3.init()
web_search = Web_Search()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

def speak(text):
  engine.say(text)
  engine.runAndWait()

def recordAudio():
  recognizer = speech_recognition.Recognizer()

  
  with speech_recognition.Microphone() as source:
    recognizer.energy_threshold = 10000
    recognizer.adjust_for_ambient_noise(source, 1)

    print("Listening...")
    audio = recognizer.listen(source)

    try:
      statement = recognizer.recognize_google(audio, language="en-US")
      print('User said: ', statement)
    except speech_recognition.UnknownValueError:
      return 'None'
    return statement

def openApp(application):
  os.startfile(application)


while True:
  text = recordAudio().lower()
  
  if 'joshua' in text:
    speak("How can I help you?")

  elif 'hello' in text or 'hi' in text or "what's up" in text or 'sup' in text:
    greetings = ['Hello', 'Hi', 'Hey']
    greeting = random.choice(greetings)

    print(greeting)
    print("How are you?")
    speak(greeting)
    speak("How are you?")

  elif 'tell' in text and 'hi' in text or 'tell' in text and 'hello' in text:
    text = text.split()
    speak("Hello, " + text[1])

  elif 'good' in text or 'great' in text or 'fine' in text:
    print("I am glad to hear that. How can I help you?")
    speak("I am glad to hear that. How can I help you?")
    
  elif 'bad' in text or 'not good' in text or 'terrible' in text or 'horrible' in text:
    print("I am sorry to hear that. How can I help you?")
    print("I am sorry to hear that. How can I help you?")
    
  elif 'how are you' in text or "how're you" in text or 'how about you' in text:
    print("I am doing good. How can I help you?")
    speak("I am doing good. How can I help you?")

  elif 'goodbye' in text or 'bye' in text or 'exit' in text or 'quit' in text or 'stop' in text:
      print("Goodbye!")
      speak("Goodbye!")
      break

  elif 'search wikipedia for' in text:
    text = text.replace('search wikipedia for', '')
    
    print('Searching Wikipedia for ', text)
    speak('Searching Wikipedia for ' + text)

    web_search.wikipedia(text)

  elif 'open wikipedia' in text:
    print('Opening Wikipedia...')
    speak('Opening Wikipedia...')

    web_search.open_page("https://www.wikipedia.org")

  elif 'search youtube for' in text:
    text = text.replace('search youtube for', '')

    print('Searching YouTube for ', text)
    speak('Searching YouTube for ' + text)

    web_search.youtube(text)

  elif 'open youtube' in text:
    print('Opening Youtube...')
    speak('Opening Youtube...')

    web_search.open_page("https://www.youtube.com")

  elif 'search for' in text or 'look up' in text:
    if 'search for' in text:
      text = text.replace('search for', '')
    elif 'look up' in text:
      text = text.replace('look up', '')

    print('Searching for ', text)
    speak('Searching for ' + text)

    web_search.duckduckgo(text)

  elif 'open vs code' in text or 'open visual studio code' in text:
    print("Opening VSCode...")
    speak("Opening VSCode...")

    openApp(START_MENU + r"Visual Studio Code\\Visual Studio Code")

  elif 'open vim' in text or 'open text editor' in text:
    print("Opening Vim...")
    speak("Opening Vim...")

    openApp(START_MENU + r"Vim 8.2\\Vim") 
  
  elif 'open rekordbox' in text:
    print("Opening RekordBox...")
    speak("Opening RekordBox...")

    openApp(START_MENU + r"Pioneer\\rekordbox 5.8.6\\rekordbox 5")
  
  elif 'open dolphin emulator' in text or 'open dolphin' in text:
    print("Opening Dolphin emulator...")
    speak("Opening Dolphin emulator...")

    openApp(START_MENU + r"Dolphin")

  elif 'open retro arch emulator' in text or 'open retro arch' in text:
    print("Opening RetroArch emulator...")
    speak("Opening RetroArch emulator...")

    openApp(START_MENU + r"RetroArch\\RetroArch")

  elif 'open files' in text or 'open explorer' in text or 'open file explorer' in text:
    print("Opening File Explorer...")
    speak("Opening File Explorer...")

    openApp(START_MENU + r"Windows System\\File Explorer")

  elif 'what time is it' in text:
    strTime = datetime.datetime.now().strftime("%H:%M")

    print(strTime)
    speak("It is " + strTime)

  else:
    print("Sorry, I don't know how to do that yet.")
    speak("Sorry, I don't know how to do that yet.")
