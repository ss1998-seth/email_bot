import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener= sr.Recognizer()
engine= pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
print('listen')

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()

    except Exception as ex:
        print(ex)


def send_email(reciever, subject, message):
    
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('shradha.seth98@gmail.com', 'Shradha@123')
    email=EmailMessage()
    email['From']='shradha.seth98@gmail.com'
    email['To']=reciever
    email['Subject']=subject
    email.set_content(message)
    server.send_message(email)
    
email_list={
    'mom':'kritika_seth@hotmail.com',
    'Dad':'sundeep.seth7@gmail.com',
    'shagun':'seth.shagun1996@gmail.com',
    'lagan':'lagansethmassmedia@gmail.com'
}
    
def get_mail_info():
    talk('To whom you want to send email')
    name= get_info()
    reciever=email_list[name]
    print(reciever)
    talk('what is the subject of the email')
    subject=get_info()
    talk('tell me the text to be displayed on your email')
    message=get_info()
    
    send_email(reciever, subject, message)

get_mail_info()    
    
