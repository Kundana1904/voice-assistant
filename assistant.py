import speech_recognition as sr
import pyttsx3
import datetime
engine=pyttsx3.init()
r=sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,destination=1);
        audio=r.listen(source)
    try:
       return r.recognize_google(audio).lower()
    except:
       return ""
speak("Hello,how can I help you")
while True:
  command=listen()
  if "time" in command:
      time=datetime.datetime.now().strftime("%H:%M")
      speak(f"The time is {time}")
  elif "hello" in command:
      speak("Hello! Nice to meet you")
  elif "stop" in command or "exit" in command:
      speak("Goodbye")
      break
