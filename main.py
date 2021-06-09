import requests
import smtplib

api_key = "f30ae11b6ff658d150a306fc60fe4a24"
email = YOUR_EMAIL
password = YOUR_PASSWORD

params = {
    "lat": 51.339695,
    "lon": 12.373075,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
data = response.json()
hours = data['hourly']
twelve_hours = hours[:12]
print(twelve_hours)
will_rain = False
for hour in twelve_hours:
    if hour['weather'][0]['id'] < 801:
        will_rain = True

if will_rain:
    message = "Bring an umbrella"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs="THE RECEIVER MAIL ID", msg=f"Subject:Rain-Alert!\n\n{message}")
        
