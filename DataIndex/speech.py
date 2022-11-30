# A simple code to play mp3 
from appFunction import *
from pygame import mixer
from plyer import notification
from readData import *

# Load book data
t = BookManager()
book = t.books[0]

mixer.init()
dir_file = "../Data/" + book.getDir()
print(total_length(dir_file))
mixer.music.load(dir_file)
mixer.music.set_volume(0.8)
play()

while True:
    # Show up a notification in window
    notification.notify(title = book.getName(), 
                        message = book.getAuthor(),
                        timeout = 0)
    print("Press p to pause, r to resume")
    print("Press e to exit")

    query = input(">>>")

    if query == 'p':
        pause()
    elif query == 'r':
        resume()
    elif query == 'e':
        exit()
        break
    elif query == 'ss':
        # back 5 second
        backward(5)
    elif query == 'sd':
        forward(5, total_length(dir_file))
    elif query == 'iv':
        increase_volume()
    elif query == 'dv':
        decrease_volume()