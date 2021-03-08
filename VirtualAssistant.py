import speech_recognition as sr
import pyttsx3
import pywhatkit as play
import datetime
import wikipedia
import pyjokes
from googlesearch import search as google

listener = sr.Recognizer()
engine = pyttsx3.init()

def alexa_talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()

    if 'what are you doing' in command:
        alexa_talk("I am talking to you right now")

    elif 'are you single' in command:
        alexa_talk("It depends")
        alexa_talk("Are you")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        alexa_talk(joke)
        print(joke)

    elif 'play' in command:
        song = command.replace('play', '')
        alexa_talk("Playing" + song)
        play.playonyt(song)

    elif 'time' in command:
        time =  datetime.datetime.now().strftime('%H:%M')
        alexa_talk("Current time is " + time)

    elif 'who is' or 'what is' in command:
        if 'who is' in command:
            command = command.replace('who is', '')
            info = wikipedia.summary(command, 1)
            print(info)
            alexa_talk(info)
        elif 'what is' in command:
            command = command.replace('what is', '')
            info = wikipedia.summary(command, 1)
            print(info)
            alexa_talk(info)

    else:
        alexa_talk("Please say the command again...")

while True:
    run_alexa()