import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    a = int(datetime.datetime.now().hour)
    if a < 12:
        speak("Good Morning sir .")
    elif a >= 12 and a <= 5:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir .")

    speak("I am Jarvis , How may i help You ?")


def takescommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1500
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said :{query}")

    except Exception as c:
        print(c)
        print("Please say that again...")
        return "none"

    return query


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshchoudhary3113@gmail.com', 'googlepassword123@')
    server.sendmail('harshchoudhary3113@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wish_me()
    while True:
        need = takescommand().lower()
        if 'wikipedia' in need:
            speak("Searching in wikipedia")
            need.replace("wikipedia", " ")
            results = wikipedia.summary(need, sentences=1)
            speak("according to wikipedia ")
            speak(results)

        elif 'open youtube' in need:
            webbrowser.get('windows-default').open("https://youtube.com/")
            # webbrowser.open("youtube.com")

        elif 'open google' in need:
            webbrowser.get('windows-default').open("https://www.google.com/")

        elif 'time' in need:
            a = str(datetime.datetime.now().strftime("%H:%M:%S"))
            speak(f"The time right now is {a}")

        elif 'spotify' in need:
            a = "C:\\Users\\Danger_Harsh\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(a)

        elif 'music' in need:
            a = "C:\\Users\\Danger_Harsh\\Desktop\\noice"
            b = os.listdir(a)
            os.startfile(os.path.join(a, b[0]))

        elif 'love' in need :
            speak("I love you too , Harsh sir !")


        elif 'send a mail' in need:
            try:
                speak("What should i say ?")
                content = takescommand()
                to = "jaye19is@cmrit.ac.in"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as r:
                print(r)
                speak("Sorry sir, I am not able to send this email")

        elif 'chess' in need:
            webbrowser.get('windows-default').open("https://www.chess.com")

        elif 'exit' in need:
            speak("Quitting the code , thank you sir .")
            exit()

        else :
            continue