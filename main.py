import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('hey my name is piku how can i help you aanand')
def take_command():
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            elif 'piku' in command:
                command = command.replace('piku', '')
                print(command)
            elif 'laptop' in command:
                command = command.replace('laptop', '')
                print(command)
            elif 'lappy' in command:
                command = command.replace('lappy', '')
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
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'what is your name' in command:
        talk('my name is piku')
    elif 'nahin bolenge' in command:
        talk('ok fine as your wish')
    elif 'Nahin bhulenge' in command:
        talk('ok fine as your wish')
    elif 'are you single' in command:
        talk('I am in a relationship with anand')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('mereko Sunai Nahin de raha hai repeate again.')


while True:
    run_alexa()