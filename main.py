import requests, json
from datetime import  datetime
# base URL
#The Author name is Gayathri
URL = "https://api.openweathermap.org/data/2.5/weather?"
#City = "Warangal"
mylocation = input("Enter the city name:")
Api_Key = "cb93812ba032e7c818e82d66ce238df7"
# upadting the URL
URL = URL + "q=" + mylocation + "&appid=" + Api_Key
# HTTP request
response = requests.get(URL)
api_data=response.json()
# checking the status code of the request
if response.status_code == 200:


   # getting data in the json format
   data = response.json()

   # getting the main dictionary block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the windspeed
   wind_spd=api_data['wind']['speed']
   #date_time
   datetime=datetime.now().strftime("%d %b %Y | %I %M %S %p")



   # weather report
   report = data['weather']
   print(f"{mylocation:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Wind_Speed: {wind_spd}",'kmph')
   print(f"DateTime: {datetime}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")