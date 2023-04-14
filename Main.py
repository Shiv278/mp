from time import sleep
import pyautogui
from types import coroutine
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import playsound
from Features import GoogleSearch
from win10toast import ToastNotifier
import subprocess
import webbrowser as web
# import wolframalpha
import ctypes
import win32com.client as wincl
import datetime
import os
# import winshell
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from pyautogui import click
import operator
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from ecapture import ecapture as ec
flag = 0
dic = ('afrikaans', 'af', 'albanian', 'sq', 
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az', 
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo', 
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)', 
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek',  'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    # kk = gTTS(audio)
    # kk.save()
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        # Speak("Hey I'm your buddy! What can I do for you?")
        print(": Listening....")
        

        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        # audio = input()


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def destination_language():
    print("Enter the language in which you\
    want to convert : Ex. Hindi , English , etc.")
    print()
      
    # Input destination language in
    # which the user wants to translate
    to_lang = TakeCommand()
    while (to_lang == "None"):
        to_lang = TakeCommand()
    to_lang = to_lang.lower()
    return to_lang

def dd():
    print("what do u want to translate?")
    query = TakeCommand()
    to_lang = destination_language()
  
# Mapping it with the code
    while (to_lang not in dic):
      print("Language in which you are trying\to convert is currently not available ,\please input some other language")
      print()
      to_lang = destination_language()
  
    to_lang = dic[dic.index(to_lang)+1]
  
  
# invoking Translator
    translator = Translator()
  
  
# Translating from src to dest
    text_to_translate = translator.translate(query, dest=to_lang)
  
    text = text_to_translate.text
  
# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because
# by default it speaks very slowly
    speak = gTTS(text=text, lang=to_lang, slow=False)
  
# Using save() method to save the translated
# speech in capture_voice.mp3
    speak.save("captured_voice.mp3")
  
# Using OS module to run the translated voice.
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')
  
# Printing Output
    print(text)

def get_operator_fn(op):
    return{
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        '/' : operator.__truediv__,
        'divided' : operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
    }[op]

def eval_binary_expr(op1,oper,op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1,op2)


def sound():
        import pywhatkit
        Speak("Tell Me The NamE oF The Song!")
        musicName = TakeCommand()

        if 'ss' in musicName:
            os.startfile('C:\\Users\\Lenovo\\Music\\ss.m4a')


        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

def TaskExe():

    while True:

        query = TakeCommand()


        if 'who am i' in query:
            Speak("If you talk then definitely you are human")
        
        elif 'open calculator' in query:
            os.system('start calc.exe')

        elif 'open notepad' in query or 'open Notepad'in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        
        elif 'open wordpad' in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')

        elif 'open camera' in query:#not working
            subprocess.Popen('C:\\Windows\\System32\\camera.exe')


        elif 'new tab' in query:
    
            press_and_release('ctrl + t')
        elif 'translator' in query:
            dd()

        elif 'close tab' in query:

            press_and_release('ctrl + w')

        elif 'calculate' in query:
            Speak("What should I do?")
            query = TakeCommand()
            print(query)
            Speak("Your result is: ")
            Speak(eval_binary_expr(*(query.split())))

        elif 'new window' in query:

            press_and_release('ctrl + n')

        elif 'history' in query:

            press_and_release('ctrl + h')

        elif 'download' in query:

            press_and_release('ctrl + j')

        elif 'bookmark' in query:

            press_and_release('ctrl + d')

            press('enter')

        elif 'incognito' in query:

            press_and_release('Ctrl + Shift + n')

        elif 'switch tab' in query:

            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

        elif 'open' in query:

            name = query.replace("open ","")

            NameA = str(name)

            if 'youtube' in NameA:

                web.open("youtube.com")

            elif 'instagram' in NameA:

                web.open("https://www.instagram.com/")


        elif 'who is Kirti' in query:
            Speak("She is a mad girl")
        
        elif 'google search' in query:
            GoogleSearch(query)
            
        elif 'play song' in query:
            sound()

        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        # elif 'calculate' in query:
        #     Speak("What to calculate?")
        #     TakeCommand()
        #     my_string = query.replace('calculate','')
        #     print(eval_binary_expr(*(my_string.split())))

        
        elif 'pause' in query:

            press('space bar')

        elif 'resume' in query:

            press('space bar')

        elif 'full screen' in query:

            press('f')

        elif 'film screen' in query:

            press('t')

        elif 'skip' in query:

            press('l')

        elif 'back' in query:

            press('j')

        elif 'increase' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + ,')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
        
        elif 'search' in query:

            click(x=667, y=146)

            Speak("What To Search Sir ?")

            search = TakeCommand()

            write(search)

            sleep(0.8)

            press('enter')

        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:

            press('m')

        elif 'my channel' in query:

            web.open("https://www.youtube.com/channel/UC7A5u12yVIZaCO_uXnNhc5g")

        # elif 'set alarm' in query:
        #     from Features import Alarm
        #     Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif "wikipedia" in query:
            web.open("wikipedia.com")

        elif "will you be my gf" in query or "will you be my bf" in query:  
            Speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            Speak("I'm fine, glad you me that")

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'online' in query:

            from Automations import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automations import TimeTable

            TimeTable()
        
        elif 'shutdown system' in query:
                Speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown /p')

        elif 'lock window' in query:
            
                Speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            Speak(f"Sir, the time is {strTime}")
        
        elif "who made you" in query or "who created you" in query:
            Speak("I have been created by Shivani.")
        
        elif "why you came to world" in query:
            Speak("Thanks to Shivani. further It's a secret")
    
        elif 'who is kirti' in query:
            Speak('Kirti is a very good girl who is always ready to help everyone')

        elif 'what is your name' in query:
            Speak('Hey my name is Jarvis')

        elif 'what is my name' in query:
            Speak('Hey Human')

        elif 'power point presentation' in query:
            Speak("opening Power Point presentation")
            power = r""
            os.startfile(power)
            
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            Speak(f"Sir, the time is {strTime}")
        
        elif 'alarm' in query:
            Speak("sir please tell time to set")
            tt=TakeCommand()
            tt=tt.replace("set alarm to ","")
            tt=tt.replace(".","")
            tt=tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif "weather" in query:
            import requests
            from bs4 import BeautifulSoup
            search = query
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_="BNeawe").text
            Speak(f"current {search} is {temp}")

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

# Getting current date and time using now().
        elif "date" in query:
# importing datetime module for now()
            import datetime

    # using now() to get current time
            current_time = datetime.datetime.now()

    # Printing value of now.
            Speak(f"date  {current_time}")
            print("Time now at greenwich meridian is:", current_time)



        # elif 'what the time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")   
        #     Speak(f"Sir, the time is {strTime}")


        elif 'play songs' in query:
            # import required module
            from playsound import playsound
  
# for playing note.wav file
            playsound('1.mp3')
            print('playing sound using  playsound')

        elif 'songs' in query:
        # import required module
            import os
            
            # play sound
            file = "note.mp3"
            print('playing sound using native player')
            os.system("mpg123 " + file)

        elif 'online' in query:

            from Automations import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automations import TimeTable

            TimeTable()

        
        elif 'send a mail' in query:
            try:
                Speak("What should I say?")
                content = TakeCommand()
                Speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                Speak("Email has been sent !")
            except Exception as e:
                print(e)
                Speak("I am not able to send this email")


        


        elif "internet speed" in query:

            import speedtest
            st=speedtest.Speedtest()
            d1=st.download()
            up=st.upload()
            Speak(f"sir we have {d1} bit per second downloading speed {up} bit per second uploading speed")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", ".jpg")
 
        # elif "restart" in query:
        #     subprocess.call(["shutdown", "/r"])
        
        elif "increase volume" in query:
           
            pyautogui.press("volumeup")

        elif "decrease volume" in query:
            pyautogui.press("volumedown")
            

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "unmute" in query:
            pyautogui.press("volumeunmute")
        
        elif 'remind me' in query:
            Speak("what should i remind you!!")
            m=TakeCommand()
            m=m.replace("remind me","")
            # Speak(m)
            Speak("in how many mins i should remind u")
            time=  TakeCommand()
            time = int(time)
            # Speak(time)
            time=time*60

# local_time = local_time * 60
# time.sleep(local_time)
            from win10toast import ToastNotifier

            n=ToastNotifier()
        
# msg=str(input())
            n.show_toast("Reminder",msg=m,duration=time)


    
        elif "send message" in query:
            # Speak("tell the number to whom the msg shoulb be sent")
            # num=TakeCommand()
            Speak("What msg should  to be send  ")
            msg=TakeCommand()
            import pywhatkit
            pywhatkit.sendwhatmsg("+91 9901794484",msg,0,0)

            # pywhatkit.sendwhatmsg("+917022423502","this is the msg sent by jarvis",10,54)
        elif 'lock window' in query:
                Speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        #  elif 'where i am ' in query:
        #     Self.location()


        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'what the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            Speak(f"Sir, the time is {strTime}")

        

        # elif 'send a mail' in query:
        #     try:
        #         Speak("What should I say?")
        #         content = TakeCommand()
        #         Speak("whome should i send")
        #         to = input()   
        #         sendEmail(to, content)
        #         Speak("Email has been sent !")
        #     except Exception as e:
        #         print(e)
        #         Speak("I am not able to send this email")


        # elif "write a note" in query:
        #     Speak("What should i write, sir")
        #     note = TakeCommand()
        #     file = open('jarvis.txt', 'w')
        #     Speak("Sir, Should i include date and time")
        #     snfm = TakeCommand()
        #     if 'yes' in snfm or 'sure' in snfm:
        #         strTime = datetime.datetime.now().strftime("% H:% M:% S")
        #         file.write(strTime)
        #         file.write(" :- ")
        #         file.write(note)
        #     else:
        #         file.write(note)
         
        # elif "show note" in query:
        #     Speak("Showing Notes")
        #     file = open("jarvis.txt", "r")
        #     print(file.read())
        #     Speak(file.read(6))
        elif "can you calculate" in query:

            op=TakeCommand()
            x=op.split()

            if(x[1]=='+'):
                Speak(int(x[0])+int(x[2]))

        elif "what is the charge" in query:
            import psutil
            battery=psutil.sensors_battery()
            percent=battery.percent
            Speak(f"sir our systemhave {percent} percent battery")

        elif 'corona cases' in query:

            from Features import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)

        
        
        

        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        #     Speak("Recycle Bin Recycled")

        
        # elif ''


        elif 'send a mail' in query:
            from Features import sendEmail
            try:

                Speak("What should I say?")
                content = TakeCommand()
                Speak("whom should i send")
                to = input("Enter Recepients mail id")    
                sendEmail(to, content)
                Speak("Email has been sent !")

            except Exception as e:
                print(e)
                Speak("I am not able to send this email")

        elif 'alarm' in query:
            import MyAlarm
            Speak("sir please tell time to set")
            tt=TakeCommand()
            tt=tt.replace("set alarm to ","")
            tt=tt.replace(".","")
            tt=tt.upper()
            # import MyAlarm
            MyAlarm.alarm(tt)
            
        elif "internet speed" in query:
    
            import speedtest
            st=speedtest.Speedtest()
            d1=st.download()
            up=st.upload()
            Speak(f"sir we have {d1} bit per second downloading speed {up} bit per second uploading speed")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", ".jpg")

        # elif "calculate" in query:
             
        #     app_id = "Wolframalpha api id"
        #     client = wolframalpha.Client(app_id)
        #     indx = query.lower().split().index('calculate')
        #     query = query.split()[indx + 1:]
        #     res = client.query(' '.join(query))
        #     answer = next(res.results).text
        #     print("The answer is " + answer)
        #     Speak("The answer is " + answer)

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:
                Speak("Thanks for giving me your time!")
                break

            elif 'exit' in query:
                Speak("Thanks for giving me your time!")
                break

            elif 'go' in query:
                Speak("Thanks for giving me your time!")
                break
            

TaskExe()