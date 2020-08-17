import time
import pyautogui
import tkinter as tk

# has been real project create this time 

def screenshot():
    name = int(round(time.time()*1000))
    name = 'D:\Real project\screenshot{}.png'.format(name)
    time.sleep(10)
    img =pyautogui.screenshot(name)
    img.show()

root =tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take screenshot",
    command = screenshot)
    
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text ="QUIT",
    command =quit)
close.pack(side=tk.LEFT)

root.mainloop()