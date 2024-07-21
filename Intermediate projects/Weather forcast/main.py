import requests
from twilio.rest import Client


adr = "https://api.openweathermap.org/data/2.5/weather"

#use your own api key from openweathermap.org
api_key= "3ae40f5988f7aff3638fb2cf29aab6a5"

#in the below fields you need to enter your credentials
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

#customise the latitude and longitude for you own location
parameters ={
    "lat": 33.571293,
    "lon":73.105670,
    "appid":api_key,
    "cnt":4
}

response =requests.get(adr , params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☔️",
    from_="YOUR TWILIO VIRTUAL NUMBER",
    to="YOUR TWILIO VERIFIED REAL NUMBER"
        )
print(message.status)