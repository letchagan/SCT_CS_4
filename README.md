
# 🧠 Basic Keylogger – Cybersecurity Internship (Task 4)

This project is a **Basic Keylogger** written in Python using the `pynput` library. Developed for **Task 4** of my **Cybersecurity Internship**, it demonstrates how keystrokes can be recorded and logged for security auditing or ethical hacking demonstrations.

---

## ⚠️ Ethical Notice

> ❗ This tool is for **educational and ethical purposes only**. Do not use it without proper authorization.

---

## ✅ Features

- Records all keys pressed on the keyboard
- Logs regular characters and special keys separately
- Saves the output to a log file (`key_log.txt`)
- Optional: Add timestamps to each keystroke

---

## 🛠️ Technologies Used

- Python 3.x
- pynput library

---

## ▶️ How to Run

1. Install the required library:
```bash
pip install pynput
```

2. Run the keylogger script:
```bash
python keylogger.py
```

3. Press keys — your input will be saved in `key_log.txt`.

4. To stop the logger, press `ESC`.

---

## 📁 Output

- All key presses will be logged in this format:
```
2025-06-30 12:35:21,453: Key pressed: a
2025-06-30 12:35:22,654: Special key pressed: Key.space
```

---

## 🙋 Developed By

**Letchagan A**  
Cybersecurity Intern  
[GitHub](https://github.com/letchagan)

---

## 📜 License

This project is licensed under the MIT License.
