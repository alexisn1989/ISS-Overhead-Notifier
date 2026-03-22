import requests
import datetime
import time
import smtplib
import os

MY_LAT = 36.8529
MY_LONG = -75.9780
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])  # ← fixed
    iss_latitude = float(data["iss_position"]["latitude"])    # ← fixed
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "date": "today",
        "timezone": "America/New_York"
    }
    response = requests.get("https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_hour = int(sunrise.split(":")[0])
    sunset_hour = int(sunset.split(":")[0]) + 12
    time_now = datetime.datetime.now().hour  
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look Up! 🛸\n\nThe ISS is overhead in Virginia Beach!"
            )
            print("Email sent!")