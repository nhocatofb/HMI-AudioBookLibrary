import _thread
import os
from tkinter import *
from tkinter import filedialog

import playsound
import speech_recognition
import speech_recognition as sr
from gtts import gTTS

from DataIndex import readData as rd
from DataIndex.appFunction import *
from Jarvis import Jarvis

root = Tk()
root.title("GUI")
root.geometry("390x600")
root.configure(bg='white')
root.resizable(False, False)

mixer.init()

playlistDir = os.getcwd() + "/Data/"


# function
def open_folder():
    # to open a file
    temp_song = filedialog.askopenfilenames(title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        # s=s.replace("D:/Ly thuyet/Nam 4/HMI/HMI-AudioBookLibrary/Data/","")
        tmp = s.rindex("/")
        s = s[tmp + 1:]
        print(s)
        playlist.insert(END, s)


def deletesong():
    curr_song = playlist.curselection()
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
convert_song_length = '00:00'
current_song = None
song_length = None
current_time = 0
is_new_song = False


def play_song():
    print("play")
    global current_song, stime, is_paused, elapsed, song_length, current_time, old
    os.chdir(path=playlistDir)
    file_dir = playlist.get(ANCHOR).split(" - ")[2]
    # music_name=playlist.get(ACTIVE)
    if (playlist.get(ANCHOR) != current_song):
        mixer.music.load(file_dir)
        current_song = playlist.get(ANCHOR)
        play()
        Label(root, image=play_icon, height=30, width=30).place(x=180, y=260)
        stime = time.time()
        is_paused = False
        current_time = 0
        old = 0
    elif (is_paused == False):
        pause()
        Label(root, image=pause_icon, height=30, width=30).place(x=180, y=260)
        is_paused = True
    else:
        resume()
        Label(root, image=play_icon, height=30, width=30).place(x=180, y=260)
        is_paused = False
    # music.config(text=music_name[0:-4])
    # get song length''
    song_length = mixer.Sound(file_dir).get_length()
    global convert_song_length
    convert_song_length = time.strftime('%M:%S', time.gmtime(song_length))
    play_time()


# Grab song length
current_time = 0
old = 0


def play_time():
    global stime, current_time, song_length, is_paused, old, is_new_song, current_song
    if is_new_song:
        is_new_song = False
        return
    if current_time >= song_length:
        current_time = 0
        is_new_song = True
        current_song = None
        play_song()
    if old == 0:
        current_time = mixer.music.get_pos() / 1000
    # print(current_time,old)
    # convert to time format
    convert = time.strftime('%M:%S', time.gmtime(current_time))
    # get current song length

    # show time in status bar
    status_bar.config(text=f'{convert} of {convert_song_length}')
    # update time
    if not is_paused:
        # print("playy")
        status_bar.after(1000, play_time)
        new = mixer.music.get_pos() / 1000
        print(new, old)
        print(current_time)
        if (new - old >= 0.5 or old == 0 or new < 0):
            current_time = current_time + 1
            old = new


def up_song():
    global current_time, is_new_song, current_song
    is_new_song = True
    # print(playlist.get(playlist.curselection()))
    for i in playlist.curselection():
        # print(i)
        if (i > 0):
            playlist.selection_clear(0, END)
            playlist.selection_set(i - 1)
            playlist.see(i - 1)
            playlist.activate(i - 1)
            playlist.selection_anchor(i - 1)
            current_time = 0
            pause()
            current_song = None
            Label(root, image=pause_icon, height=30, width=30).place(x=180, y=260)
            is_new_song = True
            play_time()
            # play_song()
        elif i == 0:
            playlist.selection_clear(0, END)
            playlist.selection_set(playlist.size() - 1)
            playlist.see(playlist.size() - 1)
            playlist.activate(playlist.size() - 1)
            playlist.selection_anchor(playlist.size() - 1)
            current_time = 0
            pause()
            current_song = None
            Label(root, image=pause_icon, height=30, width=30).place(x=180, y=260)
            is_new_song = True
            play_time()
            # play_song()
    a = playlist.get(ANCHOR).split(" - ")[0]
    print(a)
    _thread.start_new_thread(ciu, ("H?? l??", a))


def down_song():
    global current_time, is_new_song, current_song
    is_new_song = True
    for i in playlist.curselection():
        print(i)
        if (i < playlist.size() - 1):
            playlist.selection_clear(0, END)
            playlist.selection_set(i + 1)
            playlist.see(i + 1)
            playlist.activate(i + 1)
            playlist.selection_anchor(i + 1)
            current_time = 0
            pause()
            current_song = None
            Label(root, image=pause_icon, height=30, width=30).place(x=180, y=260)
            is_new_song = True
            play_time()
            # play_song()
        elif (i == playlist.size() - 1):
            playlist.selection_clear(0, END)
            playlist.selection_set(0)
            playlist.see(0)
            playlist.activate(0)
            playlist.selection_anchor(0)
            current_time = 0
            pause()
            current_song = None
            Label(root, image=pause_icon, height=30, width=30).place(x=180, y=260)
            is_new_song = True
            play_time()
            # play_song()
    a = playlist.get(ANCHOR).split(" - ")[0]
    print(a)
    _thread.start_new_thread(ciu, ("H?? l??", a))


def backward_song():
    global is_paused, elapsed, current_time, old
    if not is_paused:
        elapsed = current_time
        delta = min(elapsed, 15)
        mixer.music.play(start=elapsed - delta)
        old = 0.1
        current_time = max(elapsed - delta - 1, 0)


def forward_song():
    global current_song, is_paused, elapsed, current_time, old
    if not is_paused:
        elapsed = current_time
        delta = min(song_length - elapsed, 15)
        mixer.music.play(start=elapsed + delta)
        old = 0.1
        current_time = min(elapsed + delta - 1, song_length)


robot_ear = speech_recognition.Recognizer()
ting = os.path.dirname(__file__) + '/ting.mp3'

jarvis = Jarvis()


def speak(text):
    jarvis.speak(text)


def ciu(text, int):
    if int == "C??c t??ng gi?? tr??? b???n th??n g???p tr??m l???n":
        audio_file = os.path.dirname(__file__) + '/2.mp3'
    elif int == "Chuy???n H?? N???i":
        audio_file = os.path.dirname(__file__) + '/3.mp3'
    elif int == "Tr?? ?????i 2":
        audio_file = os.path.dirname(__file__) + '/4.mp3'
    else:
        audio_file = os.path.dirname(__file__) + '/1.mp3'
    playsound.playsound(audio_file, True)


def speak2(text):
    output = gTTS(text, lang="vi", slow=False)
    output.save("/output2.mp3")
    audio_file = os.path.dirname(__file__) + '/output2.mp3'
    playsound.playsound(audio_file, True)


def book_infor(name, author, book_type):
    info = "T??n s??ch " + name + " t??c gi??? " + author + " th??? lo???i " + book_type
    jarvis.speak(info)


def get_audio():
    playsound.playsound(ting, True)
    print("\nBot: \tListening \t *__^ \n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Me: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0


def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Kh??ng nh???n di???n ???????c kh???u l???nh")
    return 0


def help_me():
    jarvis.speak("B???n c?? th??? n??i l??n, xu???ng ????? ch???n s??ch")
    time.sleep(0.2)
    jarvis.speak("n??i ch??i ho???c b???t ????? nghe s??ch")
    time.sleep(0.2)
    jarvis.speak("ho???c n??i t???m d???ng, ti???p t???c ????? ??i???u khi???n")
    time.sleep(0.2)


def assistant_one(a, b):
    text = get_text()
    if "ch??o" in text:
        speak("ch??o")
    elif "b???t" in text or "ch??i" in text:
        play_song()
    elif "t???t" in text or "t???m d???ng" in text:
        play_song()
    elif "gi??p" in text or "h?????ng d???n" in text:
        help_me()
    elif "l??n" in text:
        up_song()
    elif "xu???ng" in text:
        down_song()
    elif "tua tr?????c" in text:
        forward_song()
    elif "tua sau" in text:
        backward_song()
    elif "????nh d???u" in text:
        book_mark(1)
    elif "????nh d???u" in text:
        open_book_mark(1)
    else:
        speak("Kh??ng th??? nh???n di???n")


def assistant(a, b):
    while True:
        text = get_text()
        if "ch??o" in text:
            speak("ch??o")
        elif "b???t" in text or "ch??i" in text:
            play_song()
        elif "t???t" in text or "t???m d???ng" in text:
            play_song()
        elif "gi??p" in text or "h?????ng d???n" in text:
            help_me()
        elif "l??n" in text:
            up_song()
        elif "xu???ng" in text:
            down_song()
        elif "tua tr?????c" in text:
            forward_song()
        elif "tua sau" in text:
            backward_song()
        elif "????nh d???u" in text:
            book_mark(1)
        elif "????nh d???u" in text:
            open_book_mark(1)
        else:
            speak("Kh??ng th??? nh???n di???n")
        if "Th??i" in text:
            break


def a():
    _thread.start_new_thread(assistant, ("Luong moi", 2,))


def b():
    _thread.start_new_thread(assistant_one, ("Luong moi", 2,))


# play/pause
play_icon = PhotoImage(file="play_icon.png")
pause_icon = PhotoImage(file="pause_icon.png")

# time
status_bar = Label(root, text="", bd=0, relief=GROOVE, anchor=E, fg="black", bg="white")
status_bar.place(x=220, y=260)

# line
line1 = PhotoImage(file="line1.png")
Label(root, image=line1, bg="white", bd=0).place(x=0, y=305)
# icon
image_icon = PhotoImage(file="book.PNG")
root.iconphoto(False, image_icon)

Circle = PhotoImage(file="round.png")
Label(root, image=Circle, bg="white", height=230, width=290).place(x=49, y=345)
# button
play_button = PhotoImage(file="play.png")
Button(root, image=play_button, height=50, width=50, command=play_song, background="white", bd=0).place(x=170, y=433)

backward_button = PhotoImage(file="slow.png")
Button(root, image=backward_button, height=50, width=50, bd=0, background="white", command=backward_song).place(x=90,
                                                                                                                y=431)

forward_button = PhotoImage(file="fast.png")
Button(root, image=forward_button, height=50, width=50, bd=0, background="white", command=forward_song).place(x=250,
                                                                                                              y=433)

up = PhotoImage(file="up.png")
Button(root, image=up, height=50, width=50, bd=0, background="white", command=up_song).place(x=170, y=362)

down = PhotoImage(file="down.png")
Button(root, image=down, height=50, width=50, bd=0, background="white", command=down_song).place(x=170, y=504)

line = PhotoImage(file="line.png")
smallbut = PhotoImage(file="smallbut.png")
Button(root, image=line, command=increase_volume).place(x=10, y=337)
Button(root, image=line, command=decrease_volume).place(x=10, y=450)
Button(root, image=line, command=a).place(x=375, y=370)
Button(root, image=smallbut, command=b).place(x=375, y=470)
# menu
# Menu=PhotoImage(file="menu.png")
# Label(root,image=Menu,bg='gray').pack(padx=10,pady=50,side=LEFT)
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=0, y=0, width=390, height=250)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg='white', fg='black', cursor="hand2",
                   yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

# initial songs
current = rd.BookManager()
for i in current.books:
    # print(i.getName()," ",i.getDir())
    playlist.insert(END, i.getName() + " - " + i.getAuthor() + " - " + i.getDir())
playlist.selection_set(0)
playlist.see(0)
playlist.activate(0)
playlist.selection_anchor(0)

root.mainloop()
