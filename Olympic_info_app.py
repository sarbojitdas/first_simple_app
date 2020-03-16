from tkinter import *
from PIL import Image, ImageTk
import webbrowser
def url_open():
    new=2
    url="https://www.olympic.org/tokyo-2020"
    
    web_open=webbrowser.open(url, new=new)
    return web_open

root=Tk()

root.title(" Information regarding Olympic 2020")

root.geometry("655x345")

label_text=Label(text="welcome to the olympic 2020 in tokyo")
label_text.grid(row=0, column=5)

image=Image.open("Tokyo_olympic.jpg")
photo=ImageTk.PhotoImage(image)

label=Label(image=photo)
label.grid(row=1, column=5)
##frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
##frame.pack(side=LEFT,anchor="nw")


b1=Button(root,fg="blue", bg="yellow", text="Click here to know details", command=url_open)
b1.grid(row=2,column=5)


root.mainloop()
