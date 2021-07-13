from gtts import gTTS 
import os

text = input("Enter string ")

langauge = 'en'

obj = gTTS(text=text,lang=langauge,slow=False)

obj.save("sample.mp3")

os.system("sample.mp3")