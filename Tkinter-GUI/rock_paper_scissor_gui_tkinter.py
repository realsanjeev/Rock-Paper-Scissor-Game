'''import library for GUI'''
import glob
import tkinter as tk
from PIL import Image, ImageTk   

IMAGE_DIR_PATH = glob.glob('*/*.png')
SIZE = (100, 100)

root = tk.Tk()
root.geometry('685x445')
root.title('Rock paper Scissor - GUI')
root.iconbitmap(bitmap='images/icon.ico')

headerFont = ("Arial bold", 30)
header = tk.Label(text='Rock Paper Scissor - Game', font=headerFont, bg='black', fg='White')
header.pack(fill='x')

image_frame = tk.Frame(root, background='gray')
image_frame.pack(expand=1, fill='both')
def result():
    '''
    result for output
    '''
    text = '''Paper cover Rock.\nRock destroy Scissor.\nScissor cut paper'''
    result_font = ('Arial bold', 25)
    result_label = tk.Label(text=text, font=result_font, fg='Gray')
    result_label.pack(side='bottom')

def whowin():
    pass


print('*'*100)
print(IMAGE_DIR_PATH)
imgs = []
for file in IMAGE_DIR_PATH:
    if file[-3:]=='png':
        im = Image.open(file)
        im.thumbnail(SIZE)
        imgs.append(ImageTk.PhotoImage(im))
        
        photo = tk.PhotoImage(file=file)
        ilabel = tk.Button(image_frame, image=imgs[-1], command=whowin, activebackground='blue')
        ilabel.pack(side='left', padx=50, pady=50, ipadx=15, ipady=25)

result()

if __name__=="__main__":
    root.mainloop()
