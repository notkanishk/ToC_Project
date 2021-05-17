from tkinter import *
import ply.lex as lex
import ply.yacc as yacc

# list of acceptable tokens
tokens = (
'INT',          # integers
'FLOAT',        # decimal numbers
'POWER',        # exponemt
'PLUS',         # addition
'MINUS',        # subtraction
'MULTIPLY',     # multiplication
'DIVIDE',       # division
'BRACKETOP',    # bracket open
'BRACKETCL',    # bracket close
)

# defining regex for the various tokens
t_POWER      = r'\^'
t_PLUS       = r'\+'
t_MINUS      = r'\-'
t_MULTIPLY   = r'\*'
t_DIVIDE     = r'\/'
t_BRACKETOP  = r'\('
t_BRACKETCL  = r'\)'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)    # changing token value data type to float from string
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    # changing token value data type to int from string
    return t

t_ignore = " \t"    # regex token for whitespace which is ignored

# handling unexpected characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    global err
    err = 1
    errDisp()

lexer = lex.lex()


#~~ driver for lexer output demo ~~#
# lexer.input('2+3')
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break
#     print(tok)


# defining token precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'NEGATIVE')
)

def p_calculate(p):
    '''
    calc : expression
         | empty
    '''
    global err
    if err == 1:
        p[1] = None
    result(str(p[1]).strip('[]'), str(calculator(p[1])))
    # print("Flat parse tree: " + str(p[1]).strip('[]'))
    # print("Result: " + str(calculator(p[1])))

def p_exp(p):
    '''
    expression : expression POWER expression
                | expression PLUS expression
                | expression MINUS expression
                | expression MULTIPLY expression
                | expression DIVIDE expression
    '''
    p[0] = (p[2], p[1], p[3])       # creating the flat parse tree

# function for expression inside brackets
def p_group(p):
    '''
    expression : BRACKETOP expression BRACKETCL
    '''
    p[0] = p[2]

# we use '%prec' to override the default precedence of MINUS to that of NEGATIVE
def p_negative(p):
    '''
    expression : MINUS expression %prec NEGATIVE
    '''
    p[0] = -p[2]

# defining the terminals
def p_terminal(p):
    '''
    expression : INT
                | FLOAT
    '''
    p[0] = p[1]

# handling unexpected expression
def p_error(p):
    if p:
        print(f"Error before {p.value}")
    else:
        print("Illegal or incomplete expression")
    global err
    err = 1
    errDisp()

# empty expression
def p_empty(p):
    'empty : '
    p[0] = None

parser = yacc.yacc()

def calculator(p):
    if type(p) is tuple:        # check if parse tree created
        if p[0] == '^':
            return calculator(p[1]) ** calculator(p[2])
        if p[0] == '+':
            return calculator(p[1]) + calculator(p[2])
        if p[0] == '-':
            return calculator(p[1]) - calculator(p[2])
        if p[0] == '*':
            return calculator(p[1]) * calculator(p[2])
        if p[0] == '/':
            return calculator(p[1]) / calculator(p[2])
    else:
        return p
err = 0
# exp = input("enter expression: ")
# parser.parse(exp)


root = Tk()
root.title("Calculator")

#~~ define functions ~~#

# tracks input from the buttons to create expression
def expIn(character):
    label1["text"] = "Enter expression:"
    currExp = entry.get()
    if currExp == "None":
        currExp = ''
    entry.delete(0, END)
    entry.insert(0, str(currExp) + str(character))
    tree.delete(0, END)
    tree.insert(0, "Press equals to calculate parse tree")
    tree.config(state=DISABLED)

# calls the parser which calls the lexer
def eval():
    label1["text"] = "Result:"
    exp = entry.get()
    global err
    err = 0
    parser.parse(exp)

# reflects the output of the parser on GUI
def result(pTree, res):
    if err == 0:
        entry.delete(0, END)
    tree.config(state=NORMAL)
    tree.delete(0, END)
    if res != "None":
        entry.insert(0, res)
    tree.insert(0, pTree)

# reflects error in parsing input expression
def errDisp():
    btClr["text"] = "CLEAR ERROR"
    btClr["bg"] = "red"
    btEqual["text"] = "Clear Error!"
    btEqual["fg"] = "red"
    btEqual["bg"] = root.cget("bg")
    btEqual.config(state=DISABLED)
    entry.delete(0, END)
    entry.insert(0, "ERROR!")
    entry["fg"] = "red"
    entry["justify"] = "center"
    btClr["padx"] = "140"
    btEqual["padx"] = "150"

# delete one character
def delOne():
    if err == 0:
        currExp = entry.get()
        entry.delete(0, END)
        currExp = currExp[:-1]
        entry.insert(0, currExp)

# resets all visual elements
def clear():
    btClr["text"] = "Clear"
    btClr["bg"] = root.cget("bg")
    btClr["padx"] = "170"
    btEqual["text"] = "="
    btEqual["fg"] = "black"
    btEqual["bg"] = "#ECA527"
    btEqual.config(state=NORMAL)
    btEqual["padx"] = "182"
    label1["text"] = "Enter expression:"
    entry["fg"] = "black"
    entry["justify"] = "right"
    entry.delete(0, END)
    tree.delete(0, END)
    tree.insert(0, "Press equals to calculate parse tree")
    tree.config(state=DISABLED)

# define visual elements
label1 = Label(text="Enter expression:")
entry = Entry(root, borderwidth=5, width=40, justify="right")
label2 = Label(text="Flat parse tree:")
tree = Entry(root, borderwidth=5, width=40, justify="center")
tree.insert(0, "Press equals to calculate parse tree")
tree.config(state=DISABLED)
blank = Label(text="")

# define number buttons
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
# define symbol buttons
btDot = Button(root, text=".", padx=42, pady=20, command= lambda: expIn('.'))
btPlus = Button(root, text="+", padx=36.5, pady=20, command= lambda: expIn('+'), bg="#F1EABC")
btMinus = Button(root, text="-", padx=40, pady=20, command= lambda: expIn('-'), bg="#F1EABC")
btBrOp = Button(root, text="(", padx=41.5, pady=20, command= lambda: expIn('('), bg="#F1EABC")
btBrCl = Button(root, text=")", padx=41.5, pady=20, command= lambda: expIn(')'), bg="#F1EABC")
btPower = Button(root, text="^", padx=38.5, pady=20, command= lambda: expIn('^'), bg="#F1EABC")
btMult = Button(root, text="x", padx=40, pady=20, command= lambda: expIn('*'), bg="#F1EABC")
btDivide = Button(root, text="/", padx=42, pady=20, command= lambda: expIn('/'), bg="#F1EABC")
btDel = Button(root, text="Del", padx=42, pady=20, command= delOne, bg="#F1EABC")
btEqual = Button(root, text="=", padx=182, pady=20, command= eval, borderwidth=3, bg="#ECA527")
btClr = Button(root, text="Clear", padx=170, pady=20, command= clear, borderwidth=4)


# making the GUI grid
label1.grid(row=0, column=0, columnspan=4, pady=5)
entry.grid(row=1, column=0, columnspan=4, padx=10)
label2.grid(row=2, column=0, columnspan=4, pady=5)
tree.grid(row=3, column=0, columnspan=4)
blank.grid(row=4, column=0, columnspan=4)
bt0.grid(row=9, column=0, columnspan=2, sticky=E+W)
bt1.grid(row=8, column=0, sticky=E+W)
bt2.grid(row=8, column=1, sticky=E+W)
bt3.grid(row=8, column=2, sticky=E+W)
bt4.grid(row=7, column=0, sticky=E+W)
bt5.grid(row=7, column=1, sticky=E+W)
bt6.grid(row=7, column=2, sticky=E+W)
bt7.grid(row=6, column=0, sticky=E+W)
bt8.grid(row=6, column=1, sticky=E+W)
bt9.grid(row=6, column=2, sticky=E+W)
btDot.grid(row=9, column=2, sticky=E+W)
btPlus.grid(row=8, column=3, sticky=E+W+N+S)
btDel.grid(row=9, column=3, sticky=E+W)
btMinus.grid(row=7, column=3, sticky=E+W)
btBrOp.grid(row=5, column=0, sticky=E+W)
btBrCl.grid(row=5, column=1, sticky=E+W)
btPower.grid(row=5, column=2, sticky=E+W)
btMult.grid(row=6, column=3, sticky=E+W)
btDivide.grid(row=5, column=3, sticky=E+W)
btEqual.grid(row=10, column=0, columnspan=4, sticky=E+W)
btClr.grid(row=11, column=0, columnspan=4, sticky=E+W)

root.mainloop()