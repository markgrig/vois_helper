from copyreg import constructor
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
import pygame

#функция для удаление файлов, в дальнейшем планируется 
#использовать подход записи файлов для голосовых сообщений с телефона
@eel.expose
def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
        print("success")
    else: print("File doesn't exists!")

#добавление проигроваемых звуков, проигрывание вступления 
pygame.init()
songLodaing = pygame.mixer.Sound('output/loading.mp3')
songExecutes  = pygame.mixer.Sound('output/executes.mp3')
songDisappearance = pygame.mixer.Sound('output/disappearance.mp3')
songAppearance = pygame.mixer.Sound('output/appearance.mp3')
pygame.mixer.music.set_volume(2)
clock = pygame.time.Clock()
songLodaing.play()

#инициализация графики 
eel.init("web")

#Инициализация синтезатора голоса  
tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', rate-40)
volume = tts.getProperty('volume')
tts.setProperty('volume', volume+0.9)
voices = tts.getProperty('voices')
NumberOfHelper = len(voices)

#Поиск голосового пакета Татьяна
i = 0
while i < NumberOfHelper:
    if 'Tatyana RSI' in voices[i].id:
        print(voices[i].id)
        tts.setProperty('voice', voices[i].id)
    i += 1

#Приветствие голосового помошника
assistantGreeting = "Привет! Меня зовут Лили'т! Чем я' могу' , вам  помо'чь? "
tts.say( assistantGreeting )
tts.runAndWait()

#Фразы, чтобы позвать помошника, или "отпустить"
releaseAssistant  = ['лилит', 'лилия', 'лиля', 'ли ли', 'лил', 'лилии', 'лилию', 'вернись',
 'ли вернись', 'ли ты где', 'бот', 'робот', 'робот', 'комп', 'компьютер' ]
callAssistant = [ 'пока', 'уйди', 'спасибо ты не нужна', 'скройся', 'исчезни', 'ты не нужна', 
'давай потом', 'затихни', 'тихо', 'жди', 'ожидай','режим ожидания', 'ожидание' ,
'протокол ждун', 'режим ждун', 'запустить режим ждун', 'режим жди', 'ждун', 'стать ждуном',
'будь ждуном', 'ты ждун', 'обожди', 'жди меня', 'помолчи','испарись'
'протокол ожидание', 'запустить протокол ожидания', 'запустить режим ожидания','всё' ]

startlisteningMode="0"

#функция говорения помощника через питон, звук воспроизводится на компьюторе
#не подходит для решений, где хотелось бы слышать ответы через телефон
def assistantSays(text):
    tts.say( text )
    tts.runAndWait()

#Класс для поиска решений Ассистентом 
class findSolution():

    def __init__(self, text): 
        self.__querval = text 
    
    def findAnswer(self):

        dirQuervals =  {
        'https://vk.com/feed': [ 'открой вк' , 'открой vk' ] ,
        'https://vk.com/im?v=' : [ 'открой сообщения' ]  ,
        'https://www.youtube.com/' : [ 'открой ютуб' ,'открой youtube'   ] ,
        'C:\Program Files (x86)\Bandicam\Loader.exe' : [ 'открой bandicam' , 'запись экрана'] ,
        'https://sber-zvuk.com/playlists' : [ 'не знаю что послушать'  ] ,
        'https://sber-zvuk.com/genres' : [ 'открой категории' ] ,
        'https://www.google.com/search?q=' : [ 'фильм', 'сериал' , 'аниме' ] ,
        'https://sber-zvuk.com/search?query=' : [ 'найди музыку' ] ,
        'https://www.google.com/search?q=' : [  'найти на google' , 'найти на гугл'  ] ,
        'https://www.youtube.com/results?search_query=' : [  'найти на youtube' , 'найти на ютуб'] ,
        'https://sber-zvuk.com/genre/hiphop':  [  "хочу хип-хоп" ,  "хочу хипхоп" , "хочу хип хоп" ] ,
        'https://sber-zvuk.com/genre/relax' : [  "хочу отдых" ] ,
        'https://sber-zvuk.com/genre/party' : [  "хочу вечеринку"] ,
        'https://sber-zvuk.com/genre/pop' : [  "хочу попсу"] ,
        'https://sber-zvuk.com/genre/sport' : [  "хочу тренировку", "хочу зарядку", "хочу спорт"] ,
        'https://sber-zvuk.com/genre/rock' : [ "хочу рок" , "рок" , "хочу rock" , "rock" ] ,
        'https://sber-zvuk.com/genre/motivation' : [ 'хочу мотивацию' , "мотивацию" , "мотивация" ] ,
        'https://sber-zvuk.com/genre/melancholy' : [  'хочу меланхолию' , "хочу погрустить" ] ,
        'https://sber-zvuk.com/genre/travel' : [  'хочу путешестовать' , 'хочу в путешествие' ] 
        }

        for answer, quervals in dirQuervals.items():
            if self.__querval  in quervals:
                return answer
        return ""
    
    def helpUser( self, Querval , text ): 
        print(Querval)
        solution = ""
        dirSolution = {
            'disk' : [ 'D:' ,  'C:' ] ,
            'url' : 'http' ,
        } 
        
        for answer, solutions in dirSolution.items():
            for i in range(len(solutions)):
                if solutions[i] in Querval:
                    solution = answer
        
        if ( solution=='url' ): 
            songAppearance.play()
            songExecutes.play()
            webbrowser.open_new(Querval)

        if 'хочу' in text:
            time.sleep(6)
            pag.click()
            time.sleep(2)
            pag.press('space')
            time.sleep(2)
            tts.say('Надеюсь вам понравиться!')
            eel.call_in_py('Надеюсь вам понравиться!')
            tts.runAndWait()


        if ( solution =='disk'):
            songAppearance.play()
            songExecutes.play()
            subprocess.Popen(Querval)



def record_volume(listeningMode):
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=1)

        print('Слушаю...')
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()


        if text in callAssistant:
            print('off')
            num_rand =  random.randint(-1000000, 1000000)

            eel.call_in_py3(text)
            eel.call_in_py('Хорошо..')
            #tts.say('Хорошо...')
            tts.save_to_file('Хорошо...', "./web/audio/answer" + str(num_rand) + ".mp3" )
            tts.runAndWait()
            listeningMode="off";

        if  text in releaseAssistant:
            
            print('on')
            num_rand =  random.randint(-1000000, 1000000)

            eel.call_in_py3(text)
            #tts.say('Да, господин! Вам.. Что-то нужно? ')
            tts.save_to_file('Да, господин! Что нужно?', "./web/audio/answer" + str(num_rand)  + ".mp3" )
            tts.runAndWait()
            listeningMode="on";

        if (listeningMode == 'on'):
            if  text in releaseAssistant:
                print('Вы позвали лилит')
            else:
                print(f'Вы сказали: {query.lower()}')
                eel.call_in_py3(text)
            
        objectSolution = findSolution(text)
        Querval = objectSolution.findAnswer()
        objectSolution.helpUser(Querval, text)
        
    except:
        if listeningMode == 'on' and startlisteningMode == 'on' : 
            tts.say('Ой, я не поняла.')
            eel.call_in_py('Ой, я не поняла.')
            tts.runAndWait()

    #print(listeningMode)
    newlisteningMode= listeningMode
    return newlisteningMode

@eel.expose
def text_talk(text):
        if text in callAssistant:
            print('off')
            #tts.say('Хорошо...')
            num_rand =  random.randint(-1000000, 1000000)

            tts.save_to_file('Хорошо...', "./web/audio/answer" + str(num_rand) + ".mp3" )
            eel.call_in_py('Хорошо...', num_rand)
            tts.runAndWait()


        if  text in releaseAssistant:
            print('on')
           
            num_rand =  random.randint(-1000000, 1000000)
            
            tts.save_to_file('Да, господин! Что нужно?', "./web/audio/answer" + str(num_rand)  + ".mp3" )
            eel.call_in_py('Да, господин! Вам.. Что-то нужно? ', num_rand)
            #tts.say('Да, господин! Вам.. Что-то нужно?')
            tts.runAndWait()

        objectSolution = findSolution(text)
        Querval = objectSolution.findAnswer()
        objectSolution.helpUser(Querval, text)
        
        return 0

@eel.expose
def call_in_js(x):
        print(x)

@eel.expose
def call_in_Li(x):
        print(x)

@eel.expose
def test_on_off(x):
    startlisteningMode = x
    if startlisteningMode=="on":
        songAppearance.play()
    if startlisteningMode=="off":
        songDisappearance.play()
    print(x)
    return startlisteningMode

def my_other_thread1():
    listeningMode="on"
    while True:
        startlisteningMode = eel.call_in_py2()()
        if startlisteningMode=="on":
            listeningMode = record_volume(listeningMode)


#eel.call_in_py("Test Py")
eel.spawn(my_other_thread1)
eel.start("helper.html", size = (1920,1080),  blocking= False)
