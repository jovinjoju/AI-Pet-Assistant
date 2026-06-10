from actions import open_app, open_file
import keyboard
import threading

from pet_ui import PetUI
from voice import speak
from emotions import react
from reminders import set_reminder

running = True

def handle_command(command):
    global running

    if not running:
        return

    command = command.lower()

    # 🔥 OPEN APP
    if command.startswith("open "):
        name = command.replace("open ", "")
        
        response = open_app(name)

        # if not app → try file
        if response == "App not found":
            response = open_file(name)

        ui.update_status(response)
        speak(response)
        return

    # NORMAL AI RESPONSE
    emotion, response = react(command)
    ui.update_emotion(emotion)
    ui.update_status(response)
    speak(response)

    if "remind me" in command:
        try:
            speak("Enter reminder message in console:")
            msg = input("Reminder message: ")

            speak("Enter time in seconds:")
            secs = int(input("Seconds: "))

            set_reminder(secs, msg, speak)
        except:
            speak("Invalid input")

def toggle_pet():
    global running
    running = not running

    print("Shortcut pressed!")

    if running:
        ui.show_pet()   # 👈 NEW
        speak("I'm awake!")
    else:
        ui.hide_pet()   # 👈 NEW
        speak("Going offline")

# ✅ Run keyboard listener in separate thread
def start_hotkey():
    keyboard.add_hotkey("ctrl+shift+p", toggle_pet)
    keyboard.wait()   # keep listening

threading.Thread(target=start_hotkey, daemon=True).start()

# UI starts AFTER thread
ui = PetUI(handle_command)

ui.run()