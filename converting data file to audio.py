from gtts import  gTTS
import os
text=open('demo.txt','r',encoding='utf-8').read()
laguage='hi'
output=gTTS(text=text,lang=laguage,slow=False)
output.save('output.mp4')
os.system('start output.mp4')