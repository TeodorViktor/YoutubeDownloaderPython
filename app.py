from tkinter import *
from pytube import YouTube
from pytube import *
from pathlib import Path


def check_entry():
    """ Get the value from the Input field """
    value = input_url.get()
    """ If the input field is Empty, then the Empty Label will show a message to the user to enter a valid URL """
    if value == "":
        message.config(text="Please Enter a Valid Youtube URL")


#   """ If the Link is Valid then start Download """'
    else:
        print(YouTube.check_availability().)
        yt = YouTube(value)
        YouTube.check_availability()
        video_title = yt.title
        path = Path(video_title + ".mp4")
        message.config(text="Please wait, the video is Downloading!")
        stream = yt.streams.first()
        stream.download()
        if path.is_file:
            print('Exist')
            message.config(text="File is Downloaded!")
        else:
            message.config(text="Error occurred. Please check the link and try again")


window = Tk()

""" Resize the Window """
window.geometry("700x500")
window.configure(bg="#fffafa")

""" Give the Window a Title """
window.title("Youtube Downloader")

""" Create a Label and Put it on Screen """
label1 = Label(window, text="Please Enter valid Youtube URL \n", bg='#fffafa', fg='red',
               font=("Times New Roman", 24, 'bold'))
label1.grid(row=0)
label1.pack()

""" Create Input field to get the Youtube Link """
input_url = Entry(width=50, borderwidth=2, font=('Times New Roman', 14), takefocus="")
input_url.focus()
input_url.pack()

""" Create a Button to start the Download in Case of Valid Links """
download_button = Button(text="Click Here To Download", borderwidth=1, fg='red', bg='#fffafa',
                         font=('Times New Roman', 16, 'bold'), command=check_entry)
download_button.pack()

""" Create an Empty Label to fill it with messages later"""
message = Label(window)
message.pack()

window.mainloop()
