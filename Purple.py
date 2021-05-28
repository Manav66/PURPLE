import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
import random
import subprocess
import psutil
#import volux
import screen_brightness_control as sbc
#from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        speak("Good Morning")

    elif hour>= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Purple. How may i help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please")
        return "none"
    
    return query

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f = open('manav.txt', 'r')
    password = f.read()
    server.login('manavvermaa666@gmail.com', password)
    server.sendmail('manavvermaa666@gmail.com', to , content)
    server.close()
    f.close

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
        
        elif 'youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

        
        elif 'google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'stack overflow' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://stackoverflow.com")

        elif 'github' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://githubcom")

        elif 'prime' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://primevideo.com")

        elif 'whatsapp' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://web.whatsapp.com")
        
        elif 'facebook' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://facebook.com")

        elif 'music' in query:
            music_dir = "G:\\Songs\\English songs\\"
            songs = os.listdir(music_dir)
            # print(songs)
            play = random.choice(songs)
            os.startfile('G:\\Songs\\English songs\\' + play)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"The time is: {strTime}")

        elif 'email' in query:
            try:
                speak("What is the receiver's email id")
                to = input()
                speak("What is the email content ?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email sent")

            except Exception as e:
                print(e)
                speak("Email not sent")

          
        #else:
         #   subprocess.call(query)

        elif 'battery' in query:

            battery = psutil.sensors_battery()
            speak(f"The battery percentage is {battery.percent}")
            speak(f"Charger plugged in {battery.power_plugged}")
            speak(f"Battery time left is {convertTime(battery.secsleft)}")

        elif 'brightness' in query:
            current_brightness = sbc.get_brightness()
            speak(f"The current brightness is : {current_brightness}")  

        elif 'shut down' in query:
            speak("COMPUTER SHUTTING DOWN")
            os.system("shutdown /s /t 30")



            





        


            
            

               

            
        
        

           
            
            



                

            

        




             


             

             
             








        

         





        
       



     









