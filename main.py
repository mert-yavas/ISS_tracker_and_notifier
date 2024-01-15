import requests
from datetime import datetime
import smtplib
import time

# Set the coordinates and email credentials
MY_LAT = "ENTER YOUR LAT"
MY_LONG = "ENTER YOUR LONG"
MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_EMAIL_APP_PASS"
RECEIVER = "RECEIVER_MAIL_ADDRESS"


def is_iss_overhead():
    # Check if the ISS is currently overhead
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if the ISS is within 5 degrees of the user's location
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True


def is_night():
    # Check if it is currently night at the user's location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0])) + 3
    sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0])) + 3
    time_now = datetime.now().hour

    # Check if the current time is outside the sunrise to sunset range
    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    # Check if it is night and the ISS is overhead, then send an email
    if is_night() and is_iss_overhead():
        time.sleep(60)
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                            msg=f"Subject: ISS Coming Hurry Up\n\n The ISS above you in the sky.")
        connection.close()
