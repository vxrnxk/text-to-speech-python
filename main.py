import pyttsx3


data = input('Enter the text: ')

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()