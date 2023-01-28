'''import library for GUI'''
import glob
import tkinter as tk
from PIL import Image, ImageTk   

IMAGE_DIR_PATH = glob.glob('*/*.png')
SIZE = (50, 50)

root = tk.Tk()
root.geometry('555x345')
root.title('Rock paper Scissor - GUI')
headerFont = ("Arial bold", 30)
header = tk.Label(text='Rock Paper Scissor - Game', font=headerFont, bg='black', fg='White')
header.pack(fill='x')

def result():
    '''
    result for output
    '''
    text = '''Paper cover Rock.\nRock destroy Scissor.\nScissor cut paper'''
    result_font = ('Arial bold', 25)
    result_label = tk.Label(text=text, font=result_font, fg='Gray')
    result_label.pack(side='bottom')


print('*'*100)
print(IMAGE_DIR_PATH)
imgs = []
for file in IMAGE_DIR_PATH:
    if file[-3:]=='png':
        im = Image.open(file)
        im.thumbnail(SIZE)
        imgs.append(ImageTk.PhotoImage(im))
        
        photo = tk.PhotoImage(file=file)
        ilabel = tk.Label(root, image=imgs[-1])
        ilabel.pack(side='left')

result()

if __name__=="__main__":
    root.mainloop()
