import pyttsx3
import speech_recognition as sr
import webbrowser as web
import pyglet
import os
from time import sleep
import pyautogui as pg
import random
import datetime

print('''
▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀
▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀
▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄

''')
def talk(text):
    print( text )
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        voice = r.recognize_google(audio, language='ru-RU') 
        print(f'[+]Распознано: {voice}')
        return voice

    except sr.UnknownValueError:
        pass

    except sr.RequestError as e:
        pass

def work(message):
    message = message.lower()

    if 'Сколько времени' in command:
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif 'Открой YouTube' in command:
        web.open("www.youtube.com")

    elif 'Открой проводник' in command:
        os.system("explorer")

    elif 'Открой Gmail' in command:
        web.open("https://mail.google.com/mail/u/0/#inbox")

    elif 'Открой браузер' in command:
        web.open("www.google.com")

    elif 'Открой переводчик' in command:
        web.open("https://translate.google.com/")

    elif 'Открой virustotal' in command:
        web.open("https://www.virustotal.com/gui/home/upload")

    elif 'Открой Вконтакте' in command:
        web.open("https://vk.com/feed")

    elif 'Открой Twitch' in command:
        web.open("https://www.twitch.tv/")

    elif 'Открой Animego' in command:
        web.open("https://animego.org/")

    elif 'Открой командную строку' in command:
        os.system("start")

    elif 'Открой папку автозагрузки' in command:
        os.system("start shell:startup")

    elif 'Открой диспетчер задач' in command:
        pg.hotkey('crtl', 'shift', 'esc')

    elif 'Щёлкни мышкой' in command:
        pg.click()

    elif 'Аминь' in command:
        mus = pyglet.resource.media("jesus.mp3")
        mus.play()
        pyglet.app.run()

    elif '9474717' in command:
        mus = pyglet.resource.media("jesus2.mp3")
        mus.play()
        pyglet.app.run()

    elif '13957264' in command:
        mus = pyglet.resource.media("13957264.mp3")
        mus.play()
        pyglet.app.run()

    elif '54736' in command:
        web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif 'Привет друг' in command:
        mus = pyglet.resource.media("hi.mp3")
        mus.play()
        pyglet.app.run()

    elif 'Привет' in command:
        mus = pyglet.resource.media("Привет2.mp3")
        mus.play()
        pyglet.app.run()

    elif 'Пока' in command:
        mus = pyglet.resource.media("Пока.mp3")
        mus.play()
        pyglet.app.run()

    elif 'Пока друг' in command:
        mus = pyglet.resource.media("Пока2.mp3")
        mus.play()
        pyglet.app.run()

    else:
        pass

while True:
    command = listen_command()
    work(command)