from tkinter import *
from pygame import mixer

window = Tk()
mixer.init()
window.geometry('300x300')
window.title("Ahmed's Python Music Player")
textLabel = Label(window, text="Play Button")
textLabel.pack()

def play_music():
    mixer.music.load("Fellin Myself.mp3")
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def set_volume(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)



photo = PhotoImage(file='round-play-button.png')
playButton = Button(window, image=photo, command=play_music)
playButton.pack()
stopPhoto = PhotoImage(file='stop-button.png')
stopButton = Button(window, image=stopPhoto, command=stop_music)
stopButton.pack()

scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.pack()




window.mainloop()