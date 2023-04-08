from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
def genarate():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name+".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_lable=Label(image=image)
    image_lable.image=image
    canvas.create_window(200,450,window=image_lable)


canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(root,text="QR GENEATOR",fg='blue',font=("Areal",30))
canvas.create_window(200, 50, window=app_label)
name_label=Label(root,text='link name')
link_label=Label(root,text="link")

canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=link_entry)

button=Button(text="Generate QR Code",command=genarate)
canvas.create_window(200, 220, window=button)

root.mainloop()
