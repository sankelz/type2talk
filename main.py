import pyttsx3

text = (input("type text here - "))

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

