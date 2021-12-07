import cv2
import speech_recognition as sr
import pyttsx3

#Setting up pyttsx3 and voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

#Defining the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

cam = cv2.VideoCapture(0)

cv2.namedWindow("Add Face")

name = ""

def takeName():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Please say the name of the person")
        #r.pause_threshold = 1 #To increase pause
        audio = r.listen(source)
        while True:
			try:
				print("Understanding...")
				query = r.recognize_google(audio, language='en-in')
				print(f"You said: {query}\n")
				name = query
				break

			except Exception:
				print("I was unable to understand that. Please say that again...")

takeName()
while True:
    check, frame = cam.read()
    cv2.imshow("Capture", frame)
    

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    
    elif k%256 == 32:
        # SPACE pressed
        img_name = name + ".jpg"
        show_pic = cv2.imwrite(img_name, frame)
        print(show_pic)

del(cam)
cv2.destroyAllWindows()
