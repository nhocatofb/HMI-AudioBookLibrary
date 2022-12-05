from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("GUI")
root.geometry("920x670")
root.configure(bg='#0f1a2b')
root.resizable(False, False)

mixer.init()

# icon
image_icon = PhotoImage(file="book.PNG")
root.iconphoto(False, image_icon)

# button
play_button = PhotoImage(file="play.png")
Button(root, image=play_button, height=50, width=50).place(x=500, y=335)

stop_button = PhotoImage(file="stop.png")
Button(root, image=stop_button, height=50, width=50).place(x=580, y=335)

pause_button = PhotoImage(file="pause.png")
Button(root, image=pause_button, height=50, width=50).place(x=660, y=335)

resume_button = PhotoImage(file="resume.png")
Button(root, image=resume_button, height=50, width=50)

# menu
# Menu=PhotoImage(file="menu.png")
# Label(root,image=Menu,bg='gray').pack(padx=10,pady=50,side=LEFT)
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=35, y=200, width=250, height=250)

Text(root, height=2, width=20).place(x=25, y=460)
Button(root, text="+ Add", width=15, height=2, font=("arial", 10), bg='#f6b26b').place(x=25, y=510)
Button(root, text="- Del", width=15, height=2, font=("arial", 10), bg='white').place(x=165, y=510)
scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg='white', fg='red', cursor="hand2",
                   yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)
root.mainloop()
