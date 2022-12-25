'''import library for GUI'''
import os
from tkinter import Tk, Label, PhotoImage

IMAGE_DIR_PATH = 'images'

root = Tk()
root.geometry('555x345')
root.title('Rock paper Scissor - GUI')
headerFont = ("Arial bold", 30)

def result():
    '''
    result for output
    '''
    text = '''Paper cover Rock.
            Rock destroy Scissor.
            Scissor cut paper'''
    result_font = ('Arial bold', 25)
    result_label = Label(text=text, font=result_font, fg='Gray')
    result_label.pack(side='bottom')

header = Label(text='Rock Paper Scissor', font=headerFont, bg='black', fg='White')
header.pack(fill='x')

for path, _, files in os.walk(IMAGE_DIR_PATH):
    for file in files:
        # print(file)
        if file[-3:] == 'PNG':
            print(file)
            photo = PhotoImage(file=os.path.join(path, file))
            print(photo)
            image_label = Label(image=photo)
            image_label.pack()
result()

if __name__=="__main__":
    root.mainloop()
