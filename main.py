import requests
import smtplib

# Set email and password to be used in order to send the rain alerts.
my_email = "some_email_adress@gmail.com"
my_password = "password"

# Get the weather data using API.
MY_LAT = 0
MY_LONG = 0
API_KEY = "ApiKey"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain in the next 12 hours and send an email with a rain alert.
will_rain = False

for n in range(0, 12):
    weather_id = weather_data["hourly"][n]["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email_adress_for_rain_alert@email.com",
                            msg="Subject:It will rain today!\n\nDon't forget to bring an umbrella!"
                            )
