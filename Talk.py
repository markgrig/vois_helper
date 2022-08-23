import apiai, json, re
import pyttsx3

import speech_recognition as sr

import webbrowser
import subprocess
import time
import psutil
import pyautogui as pag
import eel
from threading import Thread

import os
import random

@eel.expose
def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
        print("success")
    else: print("File doesn't exists!")


import pygame
pygame.init()
song = pygame.mixer.Sound('output/loading.mp3')
song1 = pygame.mixer.Sound('output/appearance.mp3')
song2 = pygame.mixer.Sound('output/disappearance.mp3')
song3 = pygame.mixer.Sound('output/bell.mp3')
pygame.mixer.music.set_volume(2)
clock = pygame.time.Clock()
song.play()

tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', rate-40)
volume = tts.getProperty('volume')
tts.setProperty('volume', volume+0.9)
voices = tts.getProperty('voices')
x_v = len(voices)
i = 0
while i < x_v:
    if 'Tatyana RSI' in voices[i].id:
        print(voices[i].id)
        tts.setProperty('voice', voices[i].id)
    i += 1


start = "Привет! Меня зовут Лили'т! Чем я' могу' , вам  помо'чь? "
#tts.say( "Hello!" )
tts.say( start )
tts.runAndWait()

back = { 'пока', 'уйди', 'спасибо ты не нужна', 'скройся', 'исчезни', 'ты не нужна', 'давай потом', 'затихни', 'тихо', 'жди', 'ожидай','режим ожидания', 'ожидание' ,
'протокол ждун', 'режим ждун', 'запустить режим ждун', 'режим жди', 'ждун', 'стать ждуном', 'будь ждуном', 'ты ждун', 'обожди', 'жди меня', 'помолчи','испарись'
'протокол ожидание', 'запустить протокол ожидания', 'запустить режим ожидания','всё' }
comeback = {'лилит', 'лилия', 'лиля', 'ли ли', 'лил', 'лилии', 'лилию', 'вернись', 'ли вернись', 'ли ты где', 'бот', 'робот', 'робот', 'комп', 'компьютер'}

startrememb="0"
rememb2 = startrememb
rememb = startrememb

eel.init("web")

def talk(text):
    tts.say( text )
    tts.runAndWait()

def querlfun(text):

    Querval = 0

    if 'открой' in text:
        if 'vk' or "вк" in text:
            Querval = 'https://vk.com/feed'
    if 'открой сообщения'in text:
        Querval =  'https://vk.com/im?v='
    if ( 'открой' or 'открой ютуб' ) in text:
         if 'youtube' or "ютуб" in text:
             Querval =  'https://www.youtube.com/'
    if 'открой сберзвук'in text:
        Querval =  'https://sber-zvuk.com/'
    if 'открой мой сайт' in text:
         Querval = 'http://localhost/scientist.php'
    if 'запусти сервер' in text:
        Querval =  'D:\Program\OpenServer\Open Server.exe'
    if 'запусти чат' in text:
         Querval =  'chat.js' ,
    if 'открой атом' in text:
         Querval =  'D:\Program\atom-1-60\Atom\atom.exe'
    if 'открой bandicam' in text:
        Querval =  'D:\Program\Bandicam\loader.exe'
    if 'открой геншин' in text:
        Querval =  'C:\Program Files\Genshin Impact\launcher.exe'
    if 'открой плейлисты сберзвук' in text:
        Querval = 'https://sber-zvuk.com/playlists'
    if 'открой категории сберзвук' in text:
        Querval =  'https://sber-zvuk.com/genres'

    if 'хочу фильм' in text:
        text = text.replace('хочу','')
        text = text + ' смотреть онлайн бесплатно в хорошем качестве'
        text =text.replace(' ','+')
        Querval = 'https://www.google.com/search?q=' + text

    if 'хочу сериал' in text:
        text = text.replace('хочу ','')
        text = text + ' смотреть онлайн бесплатно в хорошем качестве'
        text =text.replace(' ','+')
        Querval = 'https://www.google.com/search?q=' + text

    if 'хочу аниме' in text:
        text = text.replace('хочу ','')
        text = text + ' смотреть онлайн бесплатно в хорошем качестве'
        text =text.replace(' ','+')
        Querval = 'https://www.google.com/search?q=' + text

    if 'найди на' in text:

        if 'сберзвук' in text:
            text = text.replace('найди на сберзвук','')
            text =text.replace(' ','+')
            Querval = 'https://sber-zvuk.com/search?query=' + text
        if 'youtube'in text or 'ютуб '  in text:
            text = text.replace('найди на youtube','')
            text = text.replace('найди на youtube','')
            text =text.replace(' ','+')
            Querval = 'https://www.youtube.com/results?search_query=' + text
        else:
            if 'google' in text or 'гугл' in text:
                text = text.replace('найди на ','')
                text = text.replace('google','')
                text = text.replace('гугл','')
                text =text.replace(' ','+')
                Querval = 'https://www.google.com/search?q=' + text

    if 'хочу хип-хоп' in text:
        Querval = 'https://sber-zvuk.com/genre/hiphop'
    if 'хочу relax' in text or 'хочу релакс' in text:
        Querval = 'https://sber-zvuk.com/genre/relax'
    if 'хочу party' in text or 'хочу пати' in text:
        Querval = 'https://sber-zvuk.com/genre/party'
    if 'хочу попсу' in text:
        Querval = 'https://sber-zvuk.com/genre/pop'
    if 'тренировка' in text:
        Querval = 'https://sber-zvuk.com/genre/sport'
    if 'хочу rock' in text or 'хочу рок' in text:
        Querval = 'https://sber-zvuk.com/genre/rock'
    if 'хочу мотивацию' in text:
        Querval = 'https://sber-zvuk.com/genre/motivation'
    if 'хочу погрустить' in text:
        Querval = 'https://sber-zvuk.com/genre/melancholy'
    if 'хочу в дорогу' in text:
        Querval = 'https://sber-zvuk.com/genre/travel'
    if 'хочу танцевать' in text:
        Querval = 'https://sber-zvuk.com/playlist/6571612'
    if 'хочу в клуб' in text:
        Querval = 'https://sber-zvuk.com/playlist/6571191'
    if 'хочу латинских чик' in  text:
        Querval = 'https://sber-zvuk.com/playlist/7021296'
    if 'хочу хаус' in text:
        Querval = 'https://sber-zvuk.com/playlist/7021572'
    if 'хочу отдохнуть' in text:
        Querval = 'https://sber-zvuk.com/playlist/6993920'

    if 'хочу перезагрузку' in text:
        Querval = 'https://sber-zvuk.com/playlist/6856417'
    if 'хочу акустику' in text:
        Querval = 'https://sber-zvuk.com/playlist/6346741'
    if 'хочу дозу' in text:
        Querval = 'https://sber-zvuk.com/playlist/7147193'


    return Querval



def record_volume(rememb):
    #print(rememb)
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=1)

        print('Слушаю...')
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()


        if text in back:
            print('off')
            num_rand =  random.randint(-1000000, 1000000)

            eel.call_in_py3(text)
            eel.call_in_py('Хорошо..')
            #tts.say('Хорошо...')
            tts.save_to_file('Хорошо...', "./web/audio/answer" + str(num_rand) + ".mp3" )
            tts.runAndWait()
            rememb="off";

        if  text in comeback:
            
            print('on')
            num_rand =  random.randint(-1000000, 1000000)

            eel.call_in_py3(text)
            #tts.say('Да, господин! Вам.. Что-то нужно? ')
            tts.save_to_file('Да, господин! Что нужно?', "./web/audio/answer" + str(num_rand)  + ".mp3" )
            tts.runAndWait()
            rememb="on";

        if (rememb == 'on'):
            if  text in comeback:
                print('Вы позвали лилит')
            else:
                print(f'Вы сказали: {query.lower()}')
                eel.call_in_py3(text)
            #talk(text)

        Querval = querlfun(text)
        print(Querval)
        res=0

        if Querval!=0 and ('D:' in Querval or 'C:' in Querval ):
            res='disk'

        if Querval!=0 and 'http' in Querval :
            res='url'

        if Querval!=0 and 'chat.js' in Querval  :
            res='node'
        print(res)
        if ( Querval!=0 and res=='url'):
            song1.play()
            song3.play()
            webbrowser.open_new(Querval)

            pag.press('space')
            if 'хочу' in text:
                eel.call_in_py('Надеюсь вам понравиться!')
                time.sleep(6)
                pag.click()
                time.sleep(2)
                pag.press('space')
                time.sleep(2)

                num_rand =  random.randint(-1000000, 1000000)

                tts.save_to_file('Надеюсь вам понравиться!', "./web/audio/answer" + str(num_rand)  + ".mp3" )
                tts.runAndWait()
                rememb="off";

        if ( Querval!=0 and res=='disk'):
            song1.play()
            song3.play()
            subprocess.Popen(Querval)


        if ( Querval!=0 and res=='node'):
            song1.play()
            song3.play()
            x = subprocess.Popen(['start', 'powershell'], shell = True)
            x.wait()
            time.sleep(2) #чтобы компьютер успел открыть консоль
            pag.typewrite('node C:\prog\openserver\domains\localhost')

            pag.press('enter')

    except:
        if rememb == 'on' and rememb2 == 'on' :
            tts.say('Ой, я не поняла.')
            eel.call_in_py('Ой, я не поняла.')
            tts.runAndWait()

    #print(rememb)
    newrememb= rememb
    return newrememb

@eel.expose
def text_talk(text):
        if text in back:
            print('off')
            #tts.say('Хорошо...')
            num_rand =  random.randint(-1000000, 1000000)

            tts.save_to_file('Хорошо...', "./web/audio/answer" + str(num_rand) + ".mp3" )
            eel.call_in_py('Хорошо...', num_rand)
            tts.runAndWait()


        if  text in comeback:
            print('on')
           
            num_rand =  random.randint(-1000000, 1000000)
            
            tts.save_to_file('Да, господин! Что нужно?', "./web/audio/answer" + str(num_rand)  + ".mp3" )
            eel.call_in_py('Да, господин! Вам.. Что-то нужно? ', num_rand)
            #tts.say('Да, господин! Вам.. Что-то нужно?')
            tts.runAndWait()

        Querval = querlfun(text)
        print(Querval)
        res=0

        if Querval!=0 and ('D:' in Querval or 'C:' in Querval ):
            res='disk'

        if Querval!=0 and 'http' in Querval :
            res='url'

        if Querval!=0 and 'chat.js' in Querval  :
            res='node'
            print(res)
        if ( Querval!=0 and res=='url'):
            song1.play()
            song3.play()
            webbrowser.open_new(Querval)

            pag.press('space')
            if 'хочу' in text:
                time.sleep(6)
                pag.click()
                time.sleep(2)
                pag.press('space')
                time.sleep(2)
                tts.say('Надеюсь вам понравиться!')
                eel.call_in_py('Надеюсь вам понравиться!')
                tts.runAndWait()


        if ( Querval!=0 and res=='disk'):
            song1.play()
            song3.play()
            subprocess.Popen(Querval)


        if ( Querval!=0 and res=='node'):
            song1.play()
            song3.play()
            x = subprocess.Popen(['start', 'powershell'], shell = True)
            x.wait()
            time.sleep(2) #чтобы компьютер успел открыть консоль
            pag.typewrite('node d:\Program\OpenServer\domains\localhost')

            pag.press('enter')
        return 0

@eel.expose
def call_in_js(x):
        print(x)

@eel.expose
def call_in_Li(x):
        print(x)

@eel.expose
def test_on_off(x):
    rememb2 = x
    if rememb2=="on":
        song3.play()
    if rememb2=="off":
        song2.play()
    print(x)
    return rememb2

def my_other_thread1():
    rememb="on"
    while True:
        rememb2 = eel.call_in_py2()()
        if rememb2=="on":
            rememb = record_volume(rememb)




#eel.call_in_py("Test Py")
eel.spawn(my_other_thread1)
eel.start("helper.html", size = (1920,1080),  blocking= False)
