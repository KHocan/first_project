from tkinter import *
import tkinter.messagebox
import os

window = Tk()
window.title("조원진과 아이들")

filename = "note.txt"
text = Text(window)
text.pack()
menu = Menu(window)
menufile = Menu(menu)
window.config(menu = menu)
menu.add_cascade(label = "군대", menu = menufile)
def openfile():
    if os.path.isfile(filename):
        with open(filename, "r", encoding = "utf-8") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())

def savefile():
    with open(filename, "w", encoding = "utf-8") as file:
        file.write(text.get("1.0", END))

def exit():
    if tkinter.messagebox.askokcancel("Quit","다시 입대하시겠습니까?"):
        window.destroy()
def about():
    label = tkinter.messagebox.showinfo("about","조원진군대입대까지 D-3개월")

menufile.add_command(label = "입대", command = openfile)
menufile.add_command(label = "퇴소", command = savefile)
menufile.add_command(label = "제대", command = exit)
menuhelp = Menu(menu)
menu.add_cascade(label = "신병휴가", menu = menuhelp)
menuhelp.add_command(label = "휴가지 정보", command = about)




window.mainloop()







