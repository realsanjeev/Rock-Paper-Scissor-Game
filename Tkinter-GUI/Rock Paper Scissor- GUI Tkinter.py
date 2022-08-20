from tkinter import *
import os
from PIL import Image, ImageTk

IMAGE_DIR_PATH = 'images'

root = Tk()
root.geometry('555x345')
root.title('Rock paper Scissor - GUI')
headerFont = ("Arial bold", 30)

header = Label(text='Rock Paper Scissor', font=headerFont, bg='black', fg='White')
header.pack(fill='x')

for path, _, files in os.walk(IMAGE_DIR_PATH):
    for file in files:
        # print(file)
        if file[-3:] == 'PNG':
            print(file)
            photo = PhotoImage(file=os.path.join(path, file))
            image_label = Label(image=photo)
            image_label.pack()

if __name__=="__main__":
    root.mainloop()