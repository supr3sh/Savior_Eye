import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import threading

#Setting up pyttsx3 and voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

#Defining gps function
def gps():
	os.system("python ./gps.py")

#Defining object detection function
def object_det():
    os.system("python3 object_det.py --modeldir=Sample_tflite_models/")

#Defining face recognition function
def face_rec():
    os.system("python3 facial_rec.py")

#Defining add_face function
def add_face():
    os.system("python3 add_face.py")

#Defininf take command function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1 #To increase pause
        audio = r.listen(source)

        try:
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except Exception:
            print("I was unable to understand that. Please say that again...")
            return "None"
    return query

#Defining the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Defining the wish me function
def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    
    speak("I am your savior eye. Please tell me how may I help you")
if __name__ == "__main__":
    wishme()
    comand = takeCommand()
    print(comand)
if __name__ == "__main__":
    wishme()
    while True:
	# comand=takeCommand()
	comand=takeCommand()
	#Execution
	if "object" in comand.lower() or "objects" in comand.lower() or "front" in comand.lower():
	    th = threading.Thread(target=object_det)
	    th.start()
	elif "location" in comand.lower() or "gps" in comand.lower():
	    th = threading.Thread(target=gps)
	    th.start()
	elif "faces" in comand.lower() or "who" in comand.lower() or "any friend" in comand.lower():
	    th = threading.Thread(target=face_rec)
	    th.start()
	elif "add face" in comand.lower() or "add person" in comand.lower():
	    th = threading.Thread(target=add_face)
	    th.start()
		
