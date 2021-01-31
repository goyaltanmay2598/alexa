import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)
friend.say("namaste ! i am your alexa ,    what can i do for you")
friend.runAndWait()


def talk(text):
    friend.say(text)
    friend.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
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
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia ', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry , i have a headache')
    elif ' are you single' in command:
        talk('i am in realtionship with wifi')
    elif ' joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("please say the command again")


while True:
    run_alexa()
