from tkinter import *
from tkinter.messagebox import showinfo
from PIL import *
import speech_recognition as sr
import pyttsx3
import datetime


def speak(audio):

    engine.say(audio)    
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello sir, Good Morning!")    
    
    elif hour>=12 and hour<18:
        speak("Hello sir, Good Afternoon!")       
    
    else:
        speak("Hello sir, Good Evening!") 

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text1
    
def TextToSpeech():
    texttospeech = Toplevel(mainwindow)
    texttospeech.title('Text to Speech Converter')
    texttospeech.geometry('830x571')
    texttospeech.resizable(False,False)
    bgimg1 = PhotoImage(file = "C:/Mycode/Others/PythonPrograms/others/assets/say_window.png")
    limg1 = Label(texttospeech, i = bgimg1)
    Label(texttospeech, text= "Text to speech converter", font=('Algerian',16), bg='Red',wrap = True,wraplength= 450).place(x=300,y=10)
    text = Text(texttospeech, height= 5 , width= 60, font=12)
    text.place(x= 150, y=438)
    speak("Text to Speech converter")
    speakbutton = Button(texttospeech, text='Listen', bg='coral', command=lambda: speak(str(text.get(1.0, END))))
    speakbutton.place(x=400, y=538)
    limg1.pack()
    texttospeech.mainloop()
 
def SpeechToText():
    speechtotext = Toplevel(mainwindow)
    speechtotext.title('Speech-to-Text Converter')
    speechtotext.geometry("830x571")
    speechtotext.resizable(False,False)
    bgimg2 = PhotoImage(file = "C:/Mycode/Others/PythonPrograms/others/assets/listen_window.png")
    limg2 = Label(speechtotext, i = bgimg2)
    Label(speechtotext, text='Speech-to-Text Converter', font=("Algerian", 16), bg='red').place(x=280,y=5)
    text = Text(speechtotext, font=12, height=7, width=47,bg= 'light blue')
    text.place(x=210, y=80)
    speak("Speech to Text converter")
    recordbutton = Button(speechtotext, text='Record', bg='yellow', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=400, y=40)
    limg2.pack()
    speechtotext.mainloop()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice', voices[1].id)


if __name__=="__main__" :    
    
    mainwindow = Tk()
    
    wishMe()
    speak('I am Luci, your speech recognition assistant. Please tell me, how may I help you?')

    mainwindow.title('Text-To-Speech and Speech-To-Text Converter')
    mainwindow.geometry('830x571')     #(width*height)pixels
    mainwindow.resizable(False,False)
    frame = Frame(mainwindow, width=830, height=571)
    bgimg= PhotoImage(file = "C:/Mycode/Others/PythonPrograms/others/assets/main_window.png")
    limg= Label(mainwindow, i=bgimg)
    Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',font=('Algerian', 16), bg='red', wrap=True, wraplength=450).place(x=230, y=20)



    texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Algerian', 16), bg='green', command=TextToSpeech)
    texttospeechbutton.place(x=10, y=180)

    
    speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Algerian', 16), bg='green', command=SpeechToText)
    speechtotextbutton.place(x=510, y=180)

    limg.pack()
    mainwindow.mainloop()