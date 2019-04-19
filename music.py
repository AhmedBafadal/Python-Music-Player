from tkinter import *

window = Tk()
window.geometry('300x300')
window.title("Ahmed's Python Music Player")
textLabel = Label(window, text="Play Button")
textLabel.pack()

photo = PhotoImage(file='round-play-button.png')
playButton = Button(window, image=photo, command=printsomething)
playButton.pack()


window.mainloop()