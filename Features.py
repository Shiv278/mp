
import smtplib
import pywhatkit
# import Main
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    os.startfile('C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\DataBase\\ExtraPro\\start.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):

    TimeHere=  open('C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\DataBase\\ExtraPro\\Alarm.py")

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\DataBase\\Youtube')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\DataBase\\Youtube')

def SpeedTest():

    os.startfile("C:\\Users\\Asus\\Music\\How_To_Make_Jarvis\\DataBase\\Gui Programs\\SpeedTestGui.py")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")

def sendEmail(to,  content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('shivaninaik20604@gmail.com','weeyabikiwuykjfa')#weeyabikiwuykjfa
    server.sendmail('shivaninaik20604@gmail.com', to, content)
    server.close()

import datetime
import winsound


def MyAlarm(Timing):
    altime=str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))

    altime=altime[11:-3]

    oreal=altime[:2]
    oreal=int(oreal)
    Mireal=altime[3:5]
    Mireal=int(Mireal)

    print(f"Done, alarm is set for {Timing}")

    while True:
        if oreal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                # Speak("Time to wakeup")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break