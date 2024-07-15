import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("my_email")
my_password = os.getenv("my_password")
to_email = os.getenv("to_email")
api_key = os.getenv("api_key")
latitude = float(os.getenv("latitude"))
longitude = float(os.getenv("longitude"))
parameters = {
    "lat" : latitude,
    "lon" : longitude,
    "appid" : api_key,
    "cnt" : 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if int(condition_data) < 700:
        will_rain = True
    
if will_rain:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject: Weather Update\n\n It might rain today!! Be alert if going out!")
else:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject: Weather Update\n\n Its all good, no rain")



