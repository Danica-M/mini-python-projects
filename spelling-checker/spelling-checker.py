from textblob import TextBlob

#downside of this program: it only corrects it if its close to the original spelling
def checkSpelling(word):
    blob = TextBlob(word)
    correctedWord = blob.correct()
    if blob == correctedWord:
        print("Your spelling of "+word+" is already correct!", )
    else:
        print("Here's the correct spelling of ", correctedWord)


while True:
    userWord = str(input("Enter word: "))
    checkSpelling(userWord)
    again = str(input("Check another word? Y/N: "))
    if again.upper() == "N":
        break
