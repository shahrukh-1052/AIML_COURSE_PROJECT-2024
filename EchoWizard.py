import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

def take_instruction():
    try:
        with sr.Microphone() as source:
            print("listening..")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            print(instruction)
    except:
        pass
    return instruction

def run_virtual_assistant():
    instruction = take_instruction()
    if "play" in instruction:
        song = instruction.replace("play","")
        pywhatkit.playonyt(song)
        say("playing"+song)

    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%H:%M:%S %p")
        print(time)
        say("The time is "+time)

    elif "wikipedia" in instruction:
        say("looking over it")
        qsn = instruction.replace("wikipedia","")
        info=wikipedia.summary(qsn,2)
        print(info)
        say("According to the wikipedia"+info)

    elif "joke" in instruction:
        joke = pyjokes.get_joke()
        print(joke)
        say(joke)

    elif "open google" in instruction:
        webbrowser.open("google.com")

    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d-%m-%y")
        print(date)
        say("The date is " + date)

    elif "email" in instruction:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("emailsender@gmail.com","password")
        talk("What should it say?")
        body = take_instruction()
        to = "emailreciever@gmail.com"
        server.sendmail("emailsender@gmail.com",to,body)
        print("Mail sent")
        server.close()

    else:
        print("Repeat please")
        say("Can you please repeat that again")

while True:
    run_virtual_assistant()
