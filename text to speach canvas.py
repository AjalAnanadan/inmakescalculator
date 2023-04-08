from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=300,)
canvas.pack()
def texts():
    text=entery.get()
    output=gTTS(text=text,lang='en',slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')
entery=Entry(root)
canvas.create_window(200,170,window=entery)
button=Button(text='start',command=texts,bg='blue',fg='white',width=6,height=1)
canvas.create_window(200,210,window=button)
root.mainloop()


