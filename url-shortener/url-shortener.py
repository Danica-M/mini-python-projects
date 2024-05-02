import pyshorteners

def shorten():
    link = str(input("Enter url:"))
    short_url = pyshorteners.Shortener().tinyurl.short(link)
    print("Shorten url: ",short_url)

shorten()