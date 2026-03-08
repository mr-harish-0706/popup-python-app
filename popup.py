import keyboard
import pygame
import tkinter as tk
import random as r 
import sys
import os

root = tk.Tk()
root.withdraw() 

pygame.mixer.init()
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

sounds = []
for i in range(1, 8):
    sound_file = resource_path(f"assets/{i}.mp3")
    sounds.append(pygame.mixer.Sound(sound_file))

def create_window():
    popup = tk.Toplevel(root)
    popup.title("idiot")
    popup.geometry("300x100")
    
    popup.attributes("-topmost", True)

    label = tk.Label(popup, text="you are an idiot 🤪", font=("Arial", 14))
    label.pack(pady=20)

    sound = r.choice(sounds)
    sound.play()
    

def trigger_popup(event):
    root.after(0, create_window)

keyboard.on_press(trigger_popup)
root.mainloop()
