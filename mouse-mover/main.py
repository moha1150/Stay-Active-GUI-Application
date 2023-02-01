import tkinter as tk
import time
import pyautogui

def start():
    global running
    running = True
    while running:
        pyautogui.moveRel(10, 0, duration=0.2)
        pyautogui.click(clicks=1, interval=1)
        time.sleep(20)

def stop():
    global running
    running = False

root = tk.Tk()
root.geometry("400x400")

running = False

start_button = tk.Button(root, text="Start", command=start)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

root.mainloop()
