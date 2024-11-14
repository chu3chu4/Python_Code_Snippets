import requests

# Open Weather API Key cae27cae63ebb705700fc36f91b7db3a

#API_key = "cae27cae63ebb705700fc36f91b7db3a" moved it into Classs Weather Init method
"""
#lat and lon of Chicago
lat = 41.8781
lon = -87.6298

try:
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}&exclude=minutely,hourly,daily,alerts&units=metric")
    print(response.json())
except ConnectionError as e: #for reasons I don't understand, this line of code generates a lot of error messages
    print("you are not connected to network")

temp = response.json()["current"] ["temp"]

print(f"In Chicago, it is currently {temp} °C")

#API call to request weather overview with a human-readable weather summary:
#human_readable_weather_summary = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/overview?lat={lat}&lon={lon}&appid={API_key}")
"""

class Weather:
    def __init__ (self, city, lat, lon, units ="metric"):
        self.API_key = "cae27cae63ebb705700fc36f91b7db3a"
        self.city = city
        self.lat = lat
        self.lon = lon
        self.units = units
        self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&appid={self.API_key}&exclude=minutely,hourly,daily,alerts&units=metric")
            response_json = response.json()

            self.currentTemp = response_json["current"]["temp"]
            self.currentWind = response_json["current"]["wind_speed"]
        except ConnectionError as e:
            print("Connection Error")

        except requests.exceptions.RequestException as e:
            print("Error fetching data from Openweather API")


    def temp_print(self):
        print(f"it is currently {self.currentTemp} °C in {self.city}")
        print(f"the speed of the wind in {self.city} is currently {self.currentWind}")


Chicago = Weather("Chicago", 41.8781, -87.6298)
Chicago.temp_print()

Beijing = Weather ("Beijing", 39.916668, 116.383331)
Beijing.temp_print()