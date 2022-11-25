from tkinter import *
window = Tk()
window.title("사칙연산 계산기")
display = Entry(window, width = 14, bg = "white",font=('',20))
display.grid(row = 0, column= 0, columnspan= 5)

but = ["7","8","9","+","C",
       "4","5","6","-","(",
       "1","2","3","*",")",
       "0",".","=","/","%"]

row_index = 1
col_index = 0

def click(key):
    if key == "=":
        result = eval(display.get()) #eval이란?
        s = str(result)
        display.delete(0,'end')
        display.insert(0,s)
    else:
        if key == "C":
            display.delete(0, "end")
            key = ''
        
        display.insert(END, key)


for but_text in but:
    def process(t = but_text):
        click(t)
    Button(window, text= but_text, width = 5, command = process).grid(row = row_index,column = col_index)
    col_index += 1

    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()