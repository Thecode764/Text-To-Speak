import pyttsx3
engine = pyttsx3.init()
say = input("Enter Your Text:")
engine.say(say)
engine.runAndWait()