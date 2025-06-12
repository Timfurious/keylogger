# Windows Keylogger & Screenshot Sender 📋🖼️

A multi-threaded Python keylogger for Windows that logs keystrokes and periodically sends both keystrokes and screenshots to a Discord channel via a bot.  
All logs and screenshots are stored in the system’s temporary folder for stealth and easy cleanup.

---

## ✨ Features

- ⌨️ **Keystroke Logging**: Captures all keyboard input, including special keys.
- 📂 **Stealth Logging**: Stores logs in `%TEMP%\keylog.txt` for minimal footprint.
- 📸 **Screenshot Capture**: Takes regular screenshots and sends them to Discord.
- 🔒 **Thread-Safe Buffer**: Uses threading locks to avoid data loss or corruption.
- 🕵️ **Optional Console Hiding**: Can run completely hidden from the user.
- 🚀 **Automatic Discord Delivery**: Sends logs and screenshots to your specified Discord channel using a bot.
- 🧹 **Auto Cleanup**: Removes temporary screenshot files after sending.

---

## ⚙️ How it works

1. **Keystrokes** are captured and buffered in real-time.
2. Every 5 seconds, the buffer is sent to Discord and cleared.
3. Every 30 seconds, a screenshot is taken and sent to Discord.
4. All files are stored in the system’s temp directory for stealth.
5. Optionally, the console window can be hidden for full invisibility.

---

## 🛠️ Requirements

- Python 3.x
- `pynput`
- `requests`
- `Pillow`
- `pywin32`

---

## 🚨 Disclaimer

This project is for **educational and authorized testing purposes only**.  
Do not use this software on any system without explicit permission.

---
