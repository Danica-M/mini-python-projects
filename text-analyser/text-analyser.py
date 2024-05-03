from textblob import TextBlob

def analyse(text):
    blob = TextBlob(text)
    senti = blob.sentiment
    
    if senti.polarity > 0:
        print("Overall Tone: Positive")
    elif senti.polarity < 0:
        print("Overall Tone: Negative")
    else:
        print("Overall Tone: Neutral")

while True:
    userText = str(input("Text to analyse: "))
    analyse(userText)
    again = str(input("Analyse another sentiment? Y/N: "))
    if again.upper() == "N":
        break
