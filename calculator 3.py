#get user input and place it in the text field
import parser
import tkinter
from tkinter import  *
root=Tk()
root.title("calculator")
display=Entry(root)
display.grid(row=0,columnspan=6)
#adding button to the calclator

i=0
def variable(num):
    global  i
    display.insert(i,num)
    i=i+1

def clear():
    display.delete(0,END)

def undo():
    full_string=display.get()
    if len(full_string):
        newstring=full_string[0:-1]
        clear()
        display.insert(0,newstring)
    else:
        clear()

def operators(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i=i+length

def calculator():
    fullstring=display.get()
    try:
        a=parser.expr(fullstring).compile()
        result=eval(a)
        clear()

        display.insert(1,result)
    except EXCEPTION:
        clear()
        display.insert(0,"error")

Button(root,text="AC ",bg="red",fg="white",command=lambda :clear(),).grid(row=1,column=0)
Button(root,text="  <  ",bg="dark grey",fg="black",command=lambda :undo()).grid(row=1,column=1)
Button(root,text=" %  ",bg="dark grey",fg="black",command=lambda :operators("%")).grid(row=1,column=2)

Button(root,text="  1  ",bg="grey",fg="white",command=lambda :variable(1)).grid(row=2,column=0)
Button(root,text="  2  ",bg="grey",fg="white",command=lambda :variable(2)).grid(row=2,column=1)
Button(root,text="  3  ",bg="grey",fg="white",command=lambda :variable(3)).grid(row=2,column=2)
Button(root,text="  4  ",bg="grey",fg="white",command=lambda :variable(4)).grid(row=3,column=0)
Button(root,text="  5  ",bg="grey",fg="white",command=lambda :variable(5)).grid(row=3,column=1)
Button(root,text="  6  ",bg="grey",fg="white",command=lambda :variable(6)).grid(row=3,column=2)
Button(root,text="  7  ",bg="grey",fg="white",command=lambda :variable(7)).grid(row=4,column=0)
Button(root,text="  8  ",bg="grey",fg="white",command=lambda :variable(8)).grid(row=4,column=1)
Button(root,text="  9  ",bg="grey",fg="white",command=lambda :variable(9)).grid(row=4,column=2)
Button(root,text="  0  ",bg="grey",fg="white",command=lambda :variable(0)).grid(row=5,column=0)

Button(root,text="÷",bg="orange",fg="white",command=lambda :operators('/')).grid(row=1,column=3)
Button(root,text=" x",bg="orange",fg="white",command=lambda :operators('*')).grid(row=2,column=3)
Button(root,text=" -",bg="orange",fg="white",command=lambda :operators('-'),).grid(row=3,column=3)
Button(root,text="+",bg="orange",fg="white",command=lambda :operators('+')).grid(row=4,column=3)
Button(root,text="=",bg="orange",fg="white",command=lambda :calculator()).grid(row=5,column=3)
Button(root,text="x^2",bg="orange",fg="white",command=lambda :operators('**2')).grid(row=5,column=2)
Button(root,text="   .  ",bg="grey",fg="white",command=lambda :operators('.')).grid(row=5,column=1)

root.mainloop()