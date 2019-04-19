
from tkinter import *
from pygame import mixer
from tkinter import filedialog, messagebox
window = Tk()
mixer.init()
window.geometry('300x300')
window.title("Ahmed's Python Music Player")

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

def help_me():
    messagebox.showinfo("Ahmed's Music Player Support", "Play Music, Stop Music, Rewind Music, Pause Music & Change Music Volume Possible on Graphical User Interface Provided That A Song Chosen Via File Menu.\n\n Once song is chosen via File Manager, upon click of the play button last song selected will start to play.")
# Menu bar
menubar = Menu(window)
submenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label='Open',command=browse_file)
submenu.add_command(label='Exit', command=window.destroy)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
submenu.add_command(label="Help", command=help_me)


textLabel = Label(window, text="Play Button")
textLabel.pack()

def play_music():

    try:
        paused
        if not paused:
            mixer.music.unpause()
            statusbar['text'] = 'Music has resumed'
        else:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = 'Music is playing'
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = 'Music is playing'
        except:
            messagebox.showerror("File Error","File Not Found")
    else:
            mixer.music.unpause()
            statusbar['text'] = 'Music has resumed'
    
        

def stop_music():
    mixer.music.stop()
    statusbar['text'] = 'Music has stopped'

def set_volume(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)

def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = 'Music has been paused'

def rewind_music():
    play_music()
    statusbar['text'] = 'Music has been rewinded'


frame = Frame(window)
frame.pack(padx = 10, pady=10)




photo = PhotoImage(file='round-play-button.png')
playButton = Button(frame, image=photo, command=play_music)
playButton.grid(row=0, column=0, padx=10)
stopPhoto = PhotoImage(file='stop-button.png')
stopButton = Button(frame, image=stopPhoto, command=stop_music)
stopButton.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='media-pause.png')
pauseBtn = Button(frame, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)

bottomframe = Frame(window)
bottomframe.pack()

rewindPhoto = PhotoImage(file='rewind.png')
rewindButton = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindButton.grid(row=0, column=0)


scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.grid(row=0, column=1)

statusbar = Label(window, text="Please Enjoy The Music", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)


window.mainloop()