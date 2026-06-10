import threading
import time

def set_reminder(seconds, message, speak_func):
    def reminder():
        time.sleep(seconds)
        speak_func(f"Reminder: {message}")
    
    threading.Thread(target=reminder).start()