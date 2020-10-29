from gtts import gTTS
import os
#if you want to read text
#myText="Hi vaibhav karnwal, you are the best. I love it"

#if we want to read a file then 
#fh--->file handler  default function is there to open and read file as open("file name", mode--->r for read and w for write)

fh=open("text.txt","r")
myText=fh.read().replace("\n"," ") #replacing line endings with space as gTTS is unable to read it

language ='en'

output=gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()  #closing file handler
os.system("start output.mp3")

