from gtts import gTTS
import pdftotext

with open("A_Byte_of_Python_Rus_2.01.txt", "rb") as f:
    text = f.read()



obj = gTTS(text, lang = "ru")
obj.save("Byte_of_Python.mp3")