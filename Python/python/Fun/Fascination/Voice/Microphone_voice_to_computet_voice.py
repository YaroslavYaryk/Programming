from gtts import gTTS

text = "Привіт, що ти там, як ділішки, як справішки??"

obj = gTTS(text, lang = "uk")
obj.save("hw.mp3")