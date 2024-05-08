import requests 

def getForecast(city):
    #independently published console-oriented weather forecast 
    url = 'https://wttr.in/{}'.format(city)
    try:
        data = requests.get(url)
        print(data.text)
    except:
        print("Error")

c = input('Enter city: ')
getForecast(c)