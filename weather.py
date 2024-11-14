import requests

# Open Weather API Key 7b76c15c0ef7370b4e74d9638af4a8c9
try:
    response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=41.8781&lon=87.6298&exclude={part}&appid=7b76c15c0ef7370b4e74d9638af4a8c9")
    print(response.json())
#except ConnectionError as e: for reasons I don't understand, this line of code generates a lot of error messages
except:
    print("you are not connected to network")

