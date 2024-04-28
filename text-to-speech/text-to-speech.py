#install pyttsx3 module using pip install pyttsx3
import pyttsx3


def toSpeech():
    #initialise the speech engine
    engine = pyttsx3.init()
    #pass into to engine to say aloud
    engine.say(str(input("type the text here: ")))
    #execute the speech
    engine.runAndWait()


#allows user to continue using the program
while True:
    toSpeech()
    again = str(input("do you want to convert more? Y/N: "))
    if again.upper() == "N":
        break