# Stay-Active-GUI-Application
This code creates a program to help you stay active while working on your computer. It moves your mouse every 20 secs &amp; clicks once every 10 secs. Has two buttons: one to start and another to stop.

This is a Python script that creates a GUI application for keeping a user active at work. The script uses the tkinter library to create the GUI, the time library to add pauses in the script, and the pyautogui library to control the mouse.

The script contains two functions start() and stop(). The start() function is triggered when the "Start" button is clicked. It sets the global variable running to True, and enters a loop that moves the mouse 10 pixels to the right every 20 seconds and clicks the mouse every 10 seconds using the pyautogui library. The stop() function is triggered when the "Stop" button is clicked. It sets the global variable running to False, which stops the loop in the start() function.

The GUI is created using the tkinter library. A Tk object is created and its size is set to 400x400 pixels. Two buttons "Start" and "Stop" are created, and their command attribute is set to start and stop functions, respectively. The buttons are added to the GUI using the pack() method. The root.mainloop() statement starts the GUI and allows the user to interact with it.
