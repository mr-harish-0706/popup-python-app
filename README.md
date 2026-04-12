# 😂 You Are An Idiot – Keyboard Troll script

A **simple Python prank program** that opens a popup window and plays a random sound **every time a key is pressed**.

The program listens to **global keyboard events** and responds with a funny popup message:

> *"you are an idiot 🤪"*

Along with a **random sound effect**.

⚠️ This project is intended **only for fun and educational purposes**.

---

## Preview

When any key is pressed:

* A popup window appears
* A random sound plays
* Multiple popups can appear if many keys are pressed

---

## How It Works

The program uses:

* **`keyboard`** → Detects global keyboard key presses
* **`tkinter`** → Creates popup windows
* **`pygame`** → Plays audio files
* **`random`** → Selects a random sound effect

Flow:

1. The script listens for **any keyboard key press**.
2. When a key is pressed:

   * A **popup window** appears.
   * A **random sound** from the assets folder plays.
3. Every key press creates **another popup**.

---

## 📂 Project Structure

```
you-are-an-idiot/
│
├── main.py
├── README.md
└── assets/
    ├── 1.mp3
    ├── 2.mp3
    ├── 3.mp3
    ├── 4.mp3
    ├── 5.mp3
    ├── 6.mp3
    └── 7.mp3
```

---

## Requirements

Install dependencies:

```bash
pip install keyboard pygame
```

---

## ▶️ Running the Program

```bash
python popup.py
```

Now press **any key** and enjoy the chaos.

---

## ⚠️ Disclaimer

This program is **not malware** and does **not harm the system**.

It simply:

* Opens popup windows
* Plays sound effects

Use it **responsibly and only for harmless pranks**.

---

# 🛑 How to Stop the Program

Since the script listens to global keyboard events, the popup windows will keep appearing whenever a key is pressed.

The program does not have a built-in exit button.

To stop it: USE MOUSE / TRACKPAD

### Windows

Right click on Taskbar to open Task Manager

Find the running process:

python.exe (if running via Python)

or the popup.exe

Select it

Click End Task

After ending the process, the popups will stop.



### [ ⬇️ Download here](https://github.com/mr-harish-0706/popup-python-app/releases/latest)



## 📜 License

This project is open-source and free to use for learning and experimentation.

---
