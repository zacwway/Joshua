import pyttsx3
import speech_recognition
import os
from selenium import webdriver
import datetime
import random

class Joshua():
  def __init__(self):
      self.engine = pyttsx3.init()
      self.voices = self.engine.getProperty('voices')
      self.rate = self.engine.getProperty('rate')

      self.engine.setProperty('voice', self.voices[0])
      self.engine.setProperty('rate', 150)

      self.recognizer = speech_recognition.Recognizer()
      
      self.awake = False

  def speak(self, text):
    print(text)
    self.engine.say(text)
    self.engine.runAndWait()

  def recordAudio(self):
    with speech_recognition.Microphone() as source:
      self.recognizer.energy_threshold = 2000
      self.recognizer.adjust_for_ambient_noise(source, duration=1)

      print("Listening...")
      self.audio = self.recognizer.listen(source)

      try:
        self.statement = self.recognizer.recognize_google(self.audio, language="en-US")
        print("User said: " + self.statement)
      except speech_recognition.UnknownValueError:
        return 'None'
      return self.statement

  def hello(self):
    self.awake = True
    greetings = ['Hi', 'Hello', "What's up"]

    self.speak(random.choice(greetings))
    self.speak("How can I help you?")

  def goodbye(self):
    self.awake = True

    self.speak("Goodbye!")

  def openApp(self, appName, appPath):
    self.speak("Opening " + appName)

    os.startfile(appPath)

  def getTime(self):
    hours = int(datetime.datetime.now().strftime("%H"))
    minutes = int(datetime.datetime.now().strftime("%M"))

    if minutes < 10:
      minutes = '0' + str(minutes)
    else:
      minutes = str(minutes)

    if hours < 12:
      return str(hours) + ":" + minutes + " AM"
    elif hours > 12:
      hours = hours - 12
      return str(hours) + ":" + minutes + " PM"