import speech_recognition as sr

enf = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = enf.listen(source)

try:
    text = enf.recognize_google(audio)
    print("You said:", text)



except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

except Exception as e:
    print("An error occurred: {0}".format(e))
