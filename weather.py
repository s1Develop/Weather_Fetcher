import requests

# imported creds.py file to secure the API key
# did this based on the youtube video https://www.youtube.com/watch?v=CJjSOzb0IYs
import creds

#TODO
# go to https://openweathermap.org/api and copy&paste in My API keys to use

# end point URL that we want to hit. telling what data we want
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#input
city = input("Enter a city name: ")

#f"{BASE_URL}": this is going to copy and paste the value of BASE_URL
#?appid: pass along our API key as what is known as a query parameter
# q: query. So this means we are going to look for the data associated with the city.
request_url = f"{BASE_URL}?appid={creds.API_KEY}&q={city}"

#GET: retrieve information
#HEAD: retrieve resource headers
#POST: submit data to the server
#PUT: save an object at the location
#DELETE: delete the object at the location

# it is going to have a data from request_url. The data is the information associated with our city.
response = requests.get(request_url)

#checking the status code of the response
# 200 means the response was successful
if response.status_code == 200:
    data = response.json()
    #print(data) # it will get the whole raw data from the API
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather in ", city, "is ", weather)
    print("Temperature: ", city, "is ", temperature)
else:
    print("An error occured")