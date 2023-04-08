from tkinter import  *
root=Tk()
root.title("calculator")
display=Entry(root)
display.grid(row=0,columnspan=7,sticky=W+E)
#adding button to the calclator

Button(root,text="AC ",).grid(row=1,column=0)
Button(root,text="+/-",).grid(row=1,column=1)
Button(root,text=" %  ",).grid(row=1,column=2)

Button(root,text="  1  ",).grid(row=2,column=0)
Button(root,text="  2  ",).grid(row=2,column=1)
Button(root,text="  3  ",).grid(row=2,column=2)
Button(root,text="  4  ",).grid(row=3,column=0)
Button(root,text="  5  ",).grid(row=3,column=1)
Button(root,text="  6  ",).grid(row=3,column=2)
Button(root,text="  7  ",).grid(row=4,column=0)
Button(root,text="  8  ",).grid(row=4,column=1)
Button(root,text="  9  ",).grid(row=4,column=2)
Button(root,text="  0  ",).grid(row=5,column=0)

Button(root,text=" /",).grid(row=1,column=3)
Button(root,text=" x",).grid(row=2,column=3)
Button(root,text=" -",).grid(row=3,column=3)
Button(root,text="+",).grid(row=4,column=3)
Button(root,text="=",).grid(row=5,column=3)
Button(root,text="  .   ",).grid(row=5,column=2)
Button(root,text=" x^2",).grid(row=5,column=1)

root.mainloop()