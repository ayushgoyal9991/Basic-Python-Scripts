# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:22:10 2021

@author: Acer
"""

from tkinter import *
import parser
from math import factorial

root = Tk()
#root.geometry('400x600')
root.title('Calculator')

# space line
Label(root,text="").grid(row=0,columnspan=6,sticky=N+E+W+S)

# adding input
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=N+E+W+S)

#adding numerical buttons
# 1 2 3
Button(root,text='1',command=lambda:get_variables(1)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root,text='2',command=lambda:get_variables(2)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root,text='3',command=lambda:get_variables(3)).grid(row=2,column=2,sticky=N+S+E+W)

# 4 5 6
Button(root,text='4',command=lambda:get_variables(4)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text='5',command=lambda:get_variables(5)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text='6',command=lambda:get_variables(6)).grid(row=3,column=2,sticky=N+S+E+W)

# 7 8 9
Button(root,text='7',command=lambda:get_variables(7)).grid(row=4,column=0,sticky=N+S+E+W)
Button(root,text='8',command=lambda:get_variables(8)).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text='9',command=lambda:get_variables(9)).grid(row=4,column=2,sticky=N+S+E+W)
# AC 0 .
Button(root,text='AC',command=lambda:clear_all()).grid(row=5,column=0,sticky=N+S+E+W)
Button(root,text='0',command=lambda:get_variables(0)).grid(row=5,column=1,sticky=N+S+E+W)
Button(root,text='.',command=lambda:get_variables(".")).grid(row=5,column=2,sticky=N+S+E+W)

# + - * /
Button(root,text='+',command=lambda:get_operation("+")).grid(row=2,column=3,sticky=N+S+E+W)
Button(root,text='-',command=lambda:get_operation("-")).grid(row=3,column=3,sticky=N+S+E+W)
Button(root,text='*',command=lambda:get_operation("*")).grid(row=4,column=3,sticky=N+S+E+W)
Button(root,text='/',command=lambda:get_operation("/")).grid(row=5,column=3,sticky=N+S+E+W)

# pi % ( exp
Button(root,text='pi',command=lambda:get_operation("3.14")).grid(row=2,column=4,sticky=N+S+E+W)
Button(root,text='%',command=lambda:get_operation("%")).grid(row=3,column=4,sticky=N+S+E+W)
Button(root,text='(',command=lambda:get_operation("(")).grid(row=4,column=4,sticky=N+S+E+W)
Button(root,text='exp',command=lambda:get_operation("**")).grid(row=5,column=4,sticky=N+S+E+W)

# del x! ) ^2
Button(root,text='del',command=lambda:undo()).grid(row=2,column=5,sticky=N+S+E+W)
Button(root,text='x!',command=lambda:fact()).grid(row=3,column=5,sticky=N+S+E+W)
Button(root,text=')',command=lambda:get_operation(")")).grid(row=4,column=5,sticky=N+S+E+W)
Button(root,text='^2',command=lambda:get_operation("**2")).grid(row=5,column=5,sticky=N+S+E+W)

# =
Button(root,text="=",command=lambda:calculate()).grid(columnspan=6,sticky=N+S+E+W)

# defining functions

i = 0 # track input index

def get_variables(num):
    global i
    display.insert(i, num)
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)
    
def undo():
    string = display.get()
    if(len(string)):
        new_string = string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        pass

def fact():
    string = display.get()
    try:
        a = parser.expr(string).compile()
        result = eval(a)
        result = factorial(result)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def calculate():
    string = display.get()
    try:
        a = parser.expr(string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

root.mainloop()


