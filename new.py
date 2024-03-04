from tkinter import *
import mysql.connector as sql
import pyttsx3
import speech_recognition as sr
from threading import Thread
win = Tk()
win.title("This is Test Window")
win.geometry("400x400")
win.config(bg="pink")

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
       # r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        return "none"
    return text





def Speak(sound):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(sound)
    engine.runAndWait()
def login():
    if diba_k_data.get() != "" and diba2_k_data.get() != "":
        db = sql.connect(host="localhost",username="root",password="",database="test")
        cursor = db.cursor()
        cursor.execute("Select username,password From users")
        rows = cursor.fetchall()
        for row in rows:
            if diba_k_data.get() == row[0]:
                if diba2_k_data.get() == row[1]:
                    Speak("Access Granted")
                    win.destroy()
                else:
                    Speak("Access Denied Password Is Wrong")
            else:
                Speak("Access Denied Username Is Wrong")


username_lbl = Label(win,text="username",font=("gaudy old style",12,"bold")).place(x=70,y=100)
diba_k_data = StringVar()
diba = Entry(win,bd=5,textvariable=diba_k_data).place(x=150,y=100)
password_lbl = Label(win,text="password",font=("gaudy old style",12,"bold")).place(x=70,y=150)
diba2_k_data = StringVar()
diba2 = Entry(win,bd=5,textvariable=diba2_k_data,show="*").place(x=150,y=150)
button = Button(win,text="Login",bg="black",fg="white",font=("gaudy old style",10,"bold"),command=login).place(x=160,y=200,width=100)

def usern():
    Speak("What Is Your Username")
    username = takecom()
    diba_k_data.set(username)
    Speak("what is Your Password")
    password = takecom()
    diba2_k_data.set(password)
    login()
   

t1 = Thread(target=usern)
t1.start()



win.mainloop()
