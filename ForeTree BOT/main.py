import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

###------------------------------------------Welcome of user---------------------------------------------------###

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am ForeTree, a newly integrated bot which is your energy conservation mate to whom you can take advice and definetely talk. Please tell me how may I help you")

###----------------------------------------------Listening-------------------------------------------------------###

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jainaadi7102@gmail.com', '*******')
    server.sendmail('foretree@gmail.com', to, content)
    server.close()

###--------------------------------------------Run Time-------------------------------------------------------###

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open learning for nature' in query:
            webbrowser.open("learningfornature.org")


        elif 'sustainanle development' in query:
            webbrowser.open("sdgs.un.org")

        elif 'India in world' in query:
            webbrowser.open("worldbank.org/en/country/india")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to ForeTree' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "foretree@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")


###---------------------------------------------END-------------------------------------------------------###