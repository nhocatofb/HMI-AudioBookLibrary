from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
from DataIndex import readData as rd
root=Tk()
root.title("GUI")
root.geometry("920x670")
root.configure(bg='#0f1a2b')
root.resizable(False,False)

mixer.init()

playlistDir=os.getcwd()+"/Data/"
# function
def open_folder():
    #to open a file  
    temp_song=filedialog.askopenfilenames(title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
       #s=s.replace("D:/Ly thuyet/Nam 4/HMI/HMI-AudioBookLibrary/Data/","")
       tmp=s.rindex("/")
       s=s[tmp+1:]
       print(s)
       playlist.insert(END,s)

def deletesong():
    curr_song=playlist.curselection()
    playlist.delete(curr_song[0])
"""""
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
"""
def play_song():
    os.chdir(path=playlistDir)
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

#name
music=Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=200,y=150,anchor="center")
#icon
image_icon=PhotoImage(file="book.PNG")
root.iconphoto(False,image_icon)

#button
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,height=50,width=50,command=play_song).place(x=500,y=335)

stop_button=PhotoImage(file="stop.png")
Button(root,image=stop_button,height=50,width=50,command=mixer.music.stop).place(x=580,y=335)

pause_button=PhotoImage(file="pause.png")
Button(root,image=pause_button,height=50,width=50,command=mixer.music.pause).place(x=660,y=335)

resume_button=PhotoImage(file="resume.png")
Button(root,image=resume_button,height=50,width=50,command=mixer.music.unpause).place(x=740,y=335)

#menu
#Menu=PhotoImage(file="menu.png")
#Label(root,image=Menu,bg='gray').pack(padx=10,pady=50,side=LEFT)
music_frame=Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=35,y=200,width=250,height=250)

Text(root,height=2,width=20).place(x=30,y=460)
Button(root,text="+ Add",width=15,height=2,font=("arial",10),bg='#f6b26b',command=open_folder).place(x=30,y=510)
Button(root,text="- Del",width=15,height=2,font=("arial",10),bg='white',command=deletesong).place(x=170,y=510)
scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg='white',fg='red',cursor="hand2",yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

#initial songs
current=rd.BookManager()
for i in current.books:
    print(i.getName()," ",i.getDir())
    playlist.insert(END,i.getDir())

root.mainloop()