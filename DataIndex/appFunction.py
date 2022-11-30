import time
from pygame import mixer

stime = None
is_paused = False
elapsed = 0

def play():
    global stime
    mixer.music.play()
    stime = time.time()
    is_paused = False

def pause():
    global is_paused, stime, elapsed
    now = time.time()
    elapsed = now - stime
    mixer.music.pause()
    is_paused = True
    
def resume():
    global is_paused, stime, elapsed
    now = time.time()
    mixer.music.unpause()
    is_paused = False
    stime = now - elapsed

def exit():
    mixer.music.stop()

# Volume is a value from 0.0 to 1.0 representing the volume for this Sound.
# So I will set it in range 0 -> 10, increase 1 or decrease 1
# If current volume is 10 or 0, if increase or decrease, it'll not change
def increase_volume():
    current_volume = mixer.music.get_volume()
    print(current_volume)
    mixer.music.set_volume(min(current_volume + 0.1, 1))
def decrease_volume():
    current_volume = mixer.music.get_volume()
    print(current_volume)
    mixer.music.set_volume(max(0,current_volume - 0.1))
def backward(x):
    global stime, is_paused, elapsed
    if stime and not is_paused:
        elapsed = time.time() - stime
        delta = min(elapsed, x)
        # pygame.mixer.music.rewind()
        # pygame.mixer.music.set_pos(elapsed - delta)
        mixer.music.play(start=elapsed-delta)
        stime += delta 
def forward(x, total_length):
    global stime, is_paused, elapsed
    if not is_paused:
        elapsed = time.time() - stime
        delta = min(total_length - elapsed , x)
        mixer.music.play(start=elapsed+delta)
        stime -= delta

def total_length(t):
    return (mixer.Sound(t).get_length())
