from tkinter import *



root = Tk()
root.title("Calculator")

# define functions
def expIn(character):
    currExp = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(currExp) + str(character))

def eval():
    return

def clear():
    entry.delete(0, END)
    tree.delete(0, END)

# define visual elements
label1 = Label(text="Enter expression:")
entry = Entry(root, borderwidth=5, width=40)
label2 = Label(text="Flat parse tree:")
tree = Entry(root, borderwidth=5, width=40)
blank = Label(text="")

# define buttons
bt0 = Button(root, text="0", padx=86, pady=20, command= lambda: expIn(0))
bt1 = Button(root, text="1", padx=40, pady=20, command= lambda: expIn(1))
bt2 = Button(root, text="2", padx=40, pady=20, command= lambda: expIn(2))
bt3 = Button(root, text="3", padx=40, pady=20, command= lambda: expIn(3))
bt4 = Button(root, text="4", padx=40, pady=20, command= lambda: expIn(4))
bt5 = Button(root, text="5", padx=40, pady=20, command= lambda: expIn(5))
bt6 = Button(root, text="6", padx=40, pady=20, command= lambda: expIn(6))
bt7 = Button(root, text="7", padx=40, pady=20, command= lambda: expIn(7))
bt8 = Button(root, text="8", padx=40, pady=20, command= lambda: expIn(8))
bt9 = Button(root, text="9", padx=40, pady=20, command= lambda: expIn(9))
# symbols
btDot = Button(root, text=".", padx=42, pady=20, command= lambda: expIn('.'))
btPlus = Button(root, text="+", padx=36.5, pady=51, command= lambda: expIn('+'))
btMinus = Button(root, text="-", padx=40, pady=20, command= lambda: expIn('-'))
btBrOp = Button(root, text="(", padx=41.5, pady=20, command= lambda: expIn('('))
btBrCl = Button(root, text=")", padx=41.5, pady=20, command= lambda: expIn(')'))
btPower = Button(root, text="^", padx=38.5, pady=20, command= lambda: expIn('^'))
btMult = Button(root, text="x", padx=40, pady=20, command= lambda: expIn('*'))
btDivide = Button(root, text="/", padx=42, pady=20, command= lambda: expIn('/'))
btEqual = Button(root, text="=", padx=177, pady=20, command= eval, borderwidth=3)
btClr = Button(root, text="Clear", padx=165, pady=20, command= clear, borderwidth=4)


# making the grid
label1.grid(row=0, column=0, columnspan=4, pady=5)
entry.grid(row=1, column=0, columnspan=4, padx=10)
label2.grid(row=2, column=0, columnspan=4, pady=5)
tree.grid(row=3, column=0, columnspan=4)
blank.grid(row=4, column=0, columnspan=4)
bt0.grid(row=9, column=0, columnspan=2)
bt1.grid(row=8, column=0)
bt2.grid(row=8, column=1)
bt3.grid(row=8, column=2)
bt4.grid(row=7, column=0)
bt5.grid(row=7, column=1)
bt6.grid(row=7, column=2)
bt7.grid(row=6, column=0)
bt8.grid(row=6, column=1)
bt9.grid(row=6, column=2)
btDot.grid(row=9, column=2)
btPlus.grid(row=8, column=3, rowspan=2)
btMinus.grid(row=7, column=3)
btBrOp.grid(row=5, column=0)
btBrCl.grid(row=5, column=1)
btPower.grid(row=5, column=2)
btMult.grid(row=6, column=3)
btDivide.grid(row=5, column=3)
btEqual.grid(row=10, column=0, columnspan=4)
btClr.grid(row=11, column=0, columnspan=4)

root.mainloop()