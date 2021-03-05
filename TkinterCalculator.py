from tkinter import *
from random import choice
from math import pi, sin, cos, tan, factorial, sqrt, asin, acos, atan, log10, frexp

# Create the window
root = Tk()
root.title('Simple Calculator')

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

#Define Buttons

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))    
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))    
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))    
    if math == "division":
        try:
            e.insert(0, f_num / float(second_number))  
        except ZeroDivisionError: 
            e.insert(0, 'DOMAIN ERROR OR DIVIDE BY ZERO') 
    if math == "sin":
        e.insert(0, round(sin(float(second_number)), 5))
    if math == "cos":
        e.insert(0, round(cos(float(second_number)), 5))
    if math == "tan":
        e.insert(0, round(tan(float(second_number)), 5))
    if math == "tanh":
        try:
            e.insert(0, round(atan(float(second_number)), 5))
        except ValueError: 
            e.insert(0, 'DOMAIN ERROR OR DIVIDE BY ZERO')
    if math == "cosh":
        try:
            e.insert(0, round(acos(float(second_number)), 5))
        except ValueError: 
            e.insert(0, 'DOMAIN ERROR OR DIVIDE BY ZERO')
    if math == "sinh":
        try:
            e.insert(0, round(asin(float(second_number)), 5))
        except ValueError: 
            e.insert(0, 'DOMAIN ERROR OR DIVIDE BY ZERO')
    if math == "factorial":
        e.insert(0, factorial(f_num))
    if math == "sqrt":
        e.insert(0, round(sqrt(float(second_number)), 5)) 
    if math == 'mantissa':
        e.insert(0, frexp(float(f_num)))
    if math == "power":
        e.insert(0, round(f_num ** float(second_number), 5)) 
    if math == "log":
        e.insert(0, round(log10(float(second_number)), 5)) 


def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_sin():
    global math
    math = "sin"
    e.delete(0, END)

def button_cos():
    global math
    math = "cos"
    e.delete(0, END)

def button_tan(): 
    global math
    math = "tan"
    e.delete(0, END)

def button_factorial():
    first_number = e.get()
    global f_num 
    global math
    math = "factorial"
    f_num = float(first_number)
    e.delete(0, END)

def button_sqrt():
    global math
    math = "sqrt"
    e.delete(0, END)

def button_mantissa():
    first_number = e.get()
    global f_num 
    global math
    f_num = float(first_number)
    math = "mantissa"
    e.delete(0, END)


def button_sinh():
    global math
    math = "sinh"
    e.delete(0, END)

def button_cosh():
    global math
    math = "cosh"
    e.delete(0, END)

def button_tanh():
    global math
    math = "tanh"
    e.delete(0, END)

def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = float(first_number)
    e.delete(0, END)

def button_log():
    global math
    math = "log"
    e.delete(0, END)

def random_color(list_of_colors):
    return choice(list_of_colors)

#Creating the buttons
colors = ['red', 'black', 'gray', 'blue', 'yellow', 'purple', 'orange', 'green', 'white']

button_1 = Button(root, text = '1', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = '2', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = '3', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = '4', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = '5', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = '6', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = '7', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = '8', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = '9', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = '0', activebackground = choice(colors), padx = 38, pady = 20, command = lambda: button_click(0))
button_pi = Button(root, text = 'π', activebackground = choice(colors), padx = 45, pady = 20, command = lambda: button_click(pi))
button_decimal = Button(root, text = '.', activebackground =choice(colors), padx = 47, pady = 20, command = lambda: button_click('.'))

button_clear = Button(root, text = 'Clear',activebackground = choice(colors),  padx = 74, pady = 20, command = button_clear)
button_add = Button(root, text = '+', activebackground = choice(colors),  padx = 37, pady = 20, command = button_add)
button_equal = Button(root, text = '=', activebackground = choice(colors),  padx = 83, pady = 20, command = button_equal)

button_subtract = Button(root, text = '-', activebackground = choice(colors), padx = 38, pady = 20, command = button_subtract)
button_multiply = Button(root, text = '*', activebackground = choice(colors), padx = 39, pady = 20, command = button_multiply)
button_divide = Button(root, text = '/', activebackground = choice(colors), padx = 39, pady = 20, command = button_divide)

button_sin = Button(root, text = 'sin', activebackground = random_color(colors), padx = 41, pady = 20, command = button_sin)
button_cos = Button(root, text = 'cos', activebackground = choice(colors), padx = 40, pady = 20, command = button_cos)
button_tan = Button(root, text = 'tan', activebackground = choice(colors), padx = 40, pady = 20, command = button_tan)
button_factorial = Button(root, text = '!', activebackground =choice(colors), padx = 49, pady = 20, command = button_factorial)
button_sqrt = Button(root, text = '√', activebackground = choice(colors), padx = 45, pady = 20, command = button_sqrt)

button_sinh = Button(root, text = 'asin', activebackground =choice(colors), padx = 41, pady = 20, command = button_sinh)
button_cosh= Button(root, text = 'acos', activebackground = choice(colors), padx = 39, pady = 20, command = button_cosh)
button_tanh = Button(root, text = 'atan', activebackground = choice(colors), padx = 40, pady = 20, command = button_tanh)
button_power = Button(root, text = 'x^y', activebackground = choice(colors), padx = 42, pady = 20, command = button_power)
button_log = Button(root, text = 'log 10', activebackground =choice(colors), padx = 35, pady = 20, command = button_log)

#Put the buttons on the screen

button_1.grid(row = 3 , column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 6, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)

button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 4, column = 1)
button_divide.grid(row = 4, column = 2)

button_pi.grid(row = 1, column = 3)
button_sin.grid(row = 2, column = 3)
button_cos.grid(row = 3, column = 3)
button_tan.grid(row = 4, column = 3)
button_factorial.grid(row = 1, column = 4)
button_sqrt.grid(row = 6, column = 3)

button_decimal.grid(row = 5, column = 3)
button_sinh.grid(row = 2, column = 4)
button_cosh.grid(row = 3, column = 4)
button_tanh.grid(row = 4, column = 4)
button_power.grid(row = 5, column = 4)
button_log.grid(row = 6, column = 4)


root.mainloop()
