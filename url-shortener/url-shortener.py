import pyshorteners

def shorten(link):
    short_url = pyshorteners.Shortener().tinyurl.short(link)
    print("Shorten url: ",short_url)


while True:
    link = str(input("Enter url:"))
    shorten(link)
    again = str(input("Shorten another url? Y/N: "))
    if again.upper() == "N":
        break
