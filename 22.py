from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import filedialog as fd

img = None
tkimg = None

def open():
    global img, tkimg
    fname = fd.askopenfilename()
    img = Image.open(fname)
    tkimg = ImageTk.PhotoImage(img)
    canvas.create_image(250, 250, image = tkimg)
    window.update()

def quit():
    window.destroy()

def irotate():
    global img, tkimg
    out = img.rotate(45)
    tkimg = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image = tkimg)
    window.update()

def iblur():
    global img, tkimg
    out = img.filter(ImageFilter.BLUR)
    tkimg = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image = tkimg)
    window.update()


window = tk.Tk()
canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

menubar = tk.Menu(window)
window.config(menu = menubar)

menufile = tk.Menu(menubar)
menubar.add_cascade(label= "파일", menu = menufile)
menufile.add_command(label = "열기", command = open)
menufile.add_command(label = "종료", command = quit)

menuip = tk.Menu(menubar)
menubar.add_cascade(label= "이미지처리", menu = menuip)
menuip.add_command(label = "회전", command = irotate)
menuip.add_command(label = "흐리게", command = iblur)


window.mainloop()
