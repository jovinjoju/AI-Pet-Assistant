import random

emotions = ["happy", "sleepy", "excited", "angry"]

def get_emotion():
    return random.choice(emotions)

def react(command):
    command = command.lower()

    if "hello" in command:
        return "happy", "Hi there!"
    elif "sleep" in command:
        return "sleepy", "Going to sleep..."
    elif "wake" in command:
        return "excited", "I'm back!"
    elif "how are you" in command:
        return "happy", "I'm doing great!"
    else:
        return get_emotion(), "I don't understand but I'm learning!"