import sys

import cv2.cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from requests import get
#import pywhatkit as kit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")

    elif hour >=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am sweety,and i am your personal assistant Sir . please tell me how may help you.")




def takeCommand():
    #microphone input from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en_in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again plese....")
        return "none"
    return query



def sendEmail(to,content):
            server = smtplib.SMTP("smtp.gmail.com" , 587)
            server.ehlo()
            server.starttls()
            server.login('coolrajeev122@gmail.com', 'rajeev@99')
            server.sendmail('coolrajeev122@gmail.com', to, content)
            server.close()



if __name__ == '__main__':
    speak("hi i am sweety . from ramgarh engineering college.")
    wishMe()
    while True:
        query = takeCommand().lower()
               #logic for executing task based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("Acording to wikipedia")
            print(result)
            speak(result)




        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open news' in query:
            webbrowser.open("https://www.thehindu.com/")

        elif 'google' in query:
            speak("sir, what should i search on google ")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("i am searching........... ")

        elif 'music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("i am playing song ")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime  = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir.. ,the current time is.. {strTime}")

        elif 'date' in query:
            strDate = datetime.date.today()
            speak(f"Sir.. ,today date is.. {strDate}")

        elif 'day' in query:
            strDay = datetime.datetime.now().strftime("%A")
            speak(f"Sir.. ,today day is.. {strDay}")

        elif "how are you" in query:
            speak("I am fine.")

        elif "about yourself" in query:
            speak("i am sweety. am a machine. i am designed for final year project . my developer is rajeev ranjan kumar and manter is ashim kumar mahato")


        elif "ramgarh engineering college" in query:
            speak("Ramgarh Engineering College is an Indian institute of undergraduate engineering education, which was established by the Government of Jharkhand in 2013 under the public–private partnership mode. It was formerly known as Techno India Ramgarh & Government Engineering College Ramgarh. It received a grant from World Bank and the Ministry of Human Resource Development of the Government of India in 2017 under a project named Technical Education Quality Improvement Programme .")


        elif "branch" in query:
            speak("there are 5 branch in our college . computer science engineering. electrical engineering.  electronic and communication engineering. mechnical engineering . and cevil engineering")




        elif 'cmd' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "email" in query:
            try:
                speak("what you want to send ?")
                content = takeCommand().lower()
                to  = "rajeevroy794@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to ER sasank")

            except Exception as e:
                print(e)
                speak("Sorry sir ,i am not able to send this mail")
        elif "thanks" in query:
            speak("thanks for useing me sir  , have a good day.")
            sys.exit()

        speak("sir, do you have any other work")





