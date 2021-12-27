import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# try:
#     print("Google thinks you said " + r.recognize_google(audio, language= "uk-Ua"))
# except sr.UnknownValueError:
#     print("Google could not understand audio")
# except sr.RequestError as e:
#     print("Google error; {0}".format(e))  
 

#write audio to a FLAC file
with open("inharitance_add.flac", "wb") as f:
    f.write(audio.get_flac_data())