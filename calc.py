from tkinter import *
import operator
import numpy as np
import matplotlib.pyplot as plt 

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "x": operator.mul,
    "x^y": operator.pow, 
    "%": operator.mod
}
knopki = [["OFF","%","x^y","/"],["7","8","9","x"],["4","5","6","-"],["1","2","3","+"],[".","0","C","="]]


calc = Tk()
calc.geometry("310x420")
calc.title("CALCULATOR3000")
calc.config(bg = "black")
calc.resizable(0,0)
label1 = Label(calc, text = "Privet!", font = ("Digital Regular", 31,"bold"), fg = "white", bg = "black", width=11, height=2, justify='right', anchor="se")
label1.place(x=15, y = 0)

number = 0
answer = 0 
func = ''
s=''


def clicked(t):
    global s 
    s+=t
    label1.config(text = s)

def deliter():
    global s
    s=s[:-1]
    label1.config(text = s)
    if s == '':
        label1.config(text= '0')

def reminder(mathfunc):
    global s
    global number
    global func
    if not s.isalpha() and s!='':
        number = float(s)
    s = ''
    func = mathfunc
    label1.config(text = s)

def conscalc():
    global s 
    global number
    global func
    global answer
    answer = action[func](float(number),float(s))
    if answer == int(answer):
        label1.config(text = str(int(answer)))
    else: 
        label1.config(text = str(answer))
    s = str(answer)

def button(t, x, y):
    if t not in ["OFF","%","x^y","x","-","+","C","=","/"]:
        btn = Button(calc, text = t, command = lambda: clicked(t), relief = FLAT, font = ("Digital Regular", 15, "bold"), bg = "#2e2c2c", fg = "white",width=5, height=1, compound=CENTER)
        btn.place(x= 10+x,y= 120+ y)
    elif t == "OFF":
        btn = Button(calc, text = t, command = calc.destroy, relief = FLAT, font = ("Digital Regular", 15, "bold"), fg = "white", bg="red", width=5, height=1, justify="center",)
        btn.place(x= 10+x,y= 120+ y)
    elif t == "C":
        btn = Button(calc, text = t, command = deliter, relief = FLAT, font = ("Digital Regular", 15, "bold"),bg = "#2e2c2c", fg = "white",width=5, height=1)
        btn.place(x= 10+x,y= 120+ y)
    elif t in ["%","x^y","x","-","+","/"]:
        btn = Button(calc, text = t,command = lambda: reminder(t), relief = FLAT, font = ("Digital Regular", 15, "bold"), bg = "orange", fg = "white",width=5, height=1, compound=CENTER)
        btn.place(x= 10+x,y= 120+ y)
    elif t == "=":
        btn = Button(calc, text = t, command = conscalc, relief = FLAT, font = ("Digital Regular", 15, "bold"),  bg = "orange", fg = "white",width=5, height=1, compound=CENTER)
        btn.place(x= 10+x,y= 120+ y)
    else:
        btn = Button(calc, text = t, relief = FLAT, font = ("Digital Regular", 15, "bold"), fg = "black",width=5, height=1, compound=CENTER)
        btn.place(x= 10+x,y= 120+ y)
    
def second_window():
    plot = Tk()
    plot.geometry("600x420")
    plot.title("PLOTTER3000")
    plot.config(bg="black")
    plot.resizable(0,0)
    label2 = Label(plot, text = "Enter your function(s):", font = ("Digital Regular", 31,"bold"), fg = "white", bg = "black", width=25, height=2, justify='right').place(x= 3, y= 10 )
    label2 = Label(plot, text = "y1 = ", font = ("Digital Regular", 21,"bold"), fg = "white", bg = "black", width=5, height=1).place(x= 15, y= 90 )
    label2 = Label(plot, text = "y2 = ", font = ("Digital Regular", 21,"bold"), fg = "white", bg = "black", width=5, height=1).place(x= 15, y= 140 )
    ent1 = Entry(plot, width = 29, font =("Digital Regular", 21,"bold"), fg = "white", bg = "black", relief=GROOVE).place(x=100, y=90)
    ent2 = Entry(plot, width = 29, font =("Digital Regular", 21,"bold"), fg = "white", bg = "black", relief=GROOVE).place(x=100, y=140)
    
    # btn = Button(, text = t, command = lambda: clicked(t), relief = FLAT, font = ("Digital Regular", 15, "bold"), bg = "#2e2c2c", fg = "white",width=5, height=1, compound=CENTER)
    #     btn.place(x= 10+x,y= 120+ y)

    plot.mainloop()

for i in range(5):
    for j in range(4):
        button(t=knopki[i][j], x= j*75,y= i*50)
btn = Button(calc, text = "Plotting", command = second_window, relief = FLAT, font = ("Digital Regular", 15, "bold"), bg = "orange", fg = "white",width=24, height=1)
btn.place(x=6 ,y= 370)


calc.mainloop()