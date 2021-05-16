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

lexer = lex.lex()


# driver for lexer output demo
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

    print("Flat parse tree: " + str(p[1]).strip('[]'))
    print("Result: " + str(calculator(p[1])))

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

exp = input("enter expression: ")
parser.parse(exp)