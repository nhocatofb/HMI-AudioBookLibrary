from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
import time
from DataIndex import readData as rd
from DataIndex.appFunction import *
root=Tk()
root.title("GUI")
root.geometry("390x524")
root.configure(bg='white')
root.resizable(False, False)

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
convert_song_length='00:00'
def play_song():
    os.chdir(path=playlistDir)
    file_dir = playlist.get(ACTIVE).split(" - ")[2]
    #music_name=playlist.get(ACTIVE)
    mixer.music.load(file_dir)
    if (stime==None):
        play()
    if (is_paused==False and stime):
        pause()
    if (is_paused==True and stime):
        resume()
    #music.config(text=music_name[0:-4])
    #get song length
    song_length=mixer.Sound(file_dir).get_length()
    global convert_song_length
    convert_song_length=time.strftime('%M:%S',time.gmtime(song_length))
    #print(time.strftime('%H:%M:%S',time.gmtime(convert_song_length)))
    play_time()
#Grab song length
def play_time():
    #get current time
    current_time=mixer.music.get_pos()/1000
    #convert to time format
    convert=time.strftime('%M:%S',time.gmtime(current_time))
    #get current song length

    #show time in status bar
    status_bar.config(text=f'Time Elapsed: {convert} of {convert_song_length}')
    #update time
    status_bar.after(1000,play_time)
#name
status_bar=Label(root,text="",bd=0,relief=GROOVE,anchor=E,fg="black",bg="white")
status_bar.place(x=200,y=260)
#icon
image_icon=PhotoImage(file="book.PNG")
root.iconphoto(False,image_icon)

#button
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,height=50,width=50,command=play_song,background="white",bd=0).place(x=170,y=383)

slow_button=PhotoImage(file="slow.png")
Button(root,image=slow_button,height=50,width=50,bd=0,background="white").place(x=84,y=383)

fast_button=PhotoImage(file="fast.png")
Button(root,image=fast_button,height=50,width=50,bd=0,background="white").place(x=256,y=383)

up=PhotoImage(file="up.png")
Button(root,image=up,height=50,width=50,bd=0,background="white").place(x=170,y=312)

down=PhotoImage(file="down.png")
Button(root,image=down,height=50,width=50,bd=0,background="white").place(x=170,y=460)

# menu
# Menu=PhotoImage(file="menu.png")
# Label(root,image=Menu,bg='gray').pack(padx=10,pady=50,side=LEFT)
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=0, y=0, width=390, height=250)

scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg='white',fg='red',cursor="hand2",yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

#initial songs
current=rd.BookManager()
for i in current.books:
    # print(i.getName()," ",i.getDir())
    playlist.insert(END,i.getName() + " - " + i.getAuthor() + " - " + i.getDir())

root.mainloop()
