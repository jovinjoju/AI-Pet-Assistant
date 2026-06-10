import pyttsx3
import threading

def speak(text):
    def run():
        engine = pyttsx3.init()   # create fresh engine each time
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run).start()