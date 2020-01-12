from tkinter import *

#This declares the window
main = Tk()
main.title('CALCULATOR')
main.geometry("380x510")
fontStyle = "Arial"
fontSize = "40"
height = 2
width = 4
screen = Frame(main, background="grey")
screen.pack(side=TOP)
buttonF = Frame(main)
buttonF.pack(side=TOP)

#helps with not allowing users to put like 2 decimals back to back
text = ""
total = ""
point = "."
add = " + "
sub = " - "
mult = " * "
div = " / "


#functions that are used as a command in the widgets
def button1():
    global text
    text += "7"
    screen.config(text=str(text))
def button2():
    global text
    text += "8"
    screen.config(text=str(text))
def button3():
    global text
    text += "9"
    screen.config(text=str(text))
def button4():
    global text
    text += "4"
    screen.config(text=str(text))
def button5():
    global text
    text += "5"
    screen.config(text=str(text))
def button6():
    global text
    text += "6"
    screen.config(text=str(text))
def button7():
    global text
    text += "1"
    screen.config(text=str(text))
def button8():
    global text
    text += "2"
    screen.config(text=str(text))
def button9():
    global text
    text += "3"
    screen.config(text=str(text))
def button0():
    global text
    text += "0"
    screen.config(text=str(text))
def buttonpoint():
    global text, point
    text += point
    point = ""
    screen.config(text=str(text))
def buttonAdd():
    global text, add, point
    text += add
    screen.config(text=str(text))
    point = "."
def buttonSub():
    global text, sub, point
    text += sub
    point = "."
    screen.config(text=str(text))
def buttonMult():
    global text, mult, point
    text += mult
    point = "."
    screen.config(text=str(text))
def buttonDiv():
    global text, div, point
    text += div
    point = "."
    screen.config(text=str(text))
def buttonEqual():
    global text, total
    total = str(eval(text))
    text = total
    screen.config(text=(text))
def clear():
    global text, point
    point = "."
    text = ""
    screen.config(text=(text))


screen = Label(screen, font=("Arial", "44"))
button1 = Button(buttonF, text="7", activeforeground = "blue", bg="red", width=width, height=height, command=button1, font=(fontStyle, fontSize))
button2 = Button(buttonF, text="8", activeforeground = "blue", width=width, height=height, command=button2, font=(fontStyle, fontSize))
button3 = Button(buttonF, text="9", activeforeground = "blue", width=width, height=height, command=button3, font=(fontStyle, fontSize))
button4 = Button(buttonF, text="4", activeforeground = "blue", width=width, height=height, command=button4, font=(fontStyle, fontSize))
button5 = Button(buttonF, text="5", activeforeground = "blue", width=width, height=height, command=button5, font=(fontStyle, fontSize))
button6 = Button(buttonF, text="6", activeforeground = "blue", width=width, height=height, command=button6, font=(fontStyle, fontSize))
button7 = Button(buttonF, text="1", activeforeground = "blue", width=width, height=height, command=button7, font=(fontStyle, fontSize))
button8 = Button(buttonF, text="2", activeforeground = "blue", width=width, height=height, command=button8, font=(fontStyle, fontSize))
button9 = Button(buttonF, text="3", activeforeground = "blue", width=width, height=height, command=button9, font=(fontStyle, fontSize))
button0 = Button(buttonF, text="0", activeforeground = "blue", width=width, height=height, command=button0, font=(fontStyle, fontSize))
buttonpoint = Button(buttonF, text=".", activeforeground = "blue", width=width, height=height, command=buttonpoint, font=(fontStyle, fontSize))
buttonequal = Button(buttonF, text="=", activeforeground = "blue", width=width, height=height, command=buttonEqual, font=(fontStyle, fontSize))
bAdd = Button(buttonF, text="+", activeforeground = "blue", width=width, height=height, command=buttonAdd, font=(fontStyle, fontSize))
bSub = Button(buttonF, text="-", activeforeground = "blue", width=width, height=height, command=buttonSub, font=(fontStyle, fontSize))
bMult = Button(buttonF, text="*", activeforeground = "blue", width=width, height=height, command=buttonMult, font=(fontStyle, fontSize))
bDiv = Button(buttonF, text="/", activeforeground = "blue", width=width, height=height, command=buttonDiv, font=(fontStyle, fontSize))
bClear = Button(main, text="CLEAR", command=clear, height=height, width=50, font=("Arial", "30"))


screen.pack(side=LEFT)
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
bAdd.grid(row = 0, column = 3)
button4.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1)
button6.grid(row = 1, column = 2)
bSub.grid(row = 1, column = 3)
button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)
bMult.grid(row = 2, column = 3)
button0.grid(row = 3, column = 0)
buttonpoint.grid(row = 3, column = 1)
buttonequal.grid(row = 3, column = 2)
bDiv.grid(row = 3, column = 3)
bClear.pack(side=BOTTOM)

#mainloop is an infinite loop which keeps the window open
main.mainloop()
