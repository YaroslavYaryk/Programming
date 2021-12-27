import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index = 1) as source:
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Google thinks you said " + r.recognize_google(audio, language= "uk-Ua"))
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Google error; {0}".format(e))        