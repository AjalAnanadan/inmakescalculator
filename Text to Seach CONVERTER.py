word=input("enter the sentance")

from gtts import gTTS
import  os
text=word
output=gTTS(text=word,lang="en",slow=False)
output.save('output.mp3')
os.system('start output.mp3')

