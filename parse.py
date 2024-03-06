import requests
from bs4 import BeautifulSoup
import time
import random

url = "target website url" #insert the url of your target site
discord_webhook_url = "your discord bot webhook" #insert the url of your discord bot webhook
discord_user_id = "your discord user id" #insert your own Discord user ID 

min_interval = 420 #minimum trigger interval 
max_interval = 1800 #maximum trigger interval

def send_discord_notification(message):
    payload = {"content": message}
    requests.post(discord_webhook_url, json=payload)

while True:
    interval = random.randint(min_interval, max_interval)
    time.sleep(interval)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    booking_status_div = soup.find('div', class_='"dl-text dl-text-title dl-text-bold dl-text-l" data-design-system="oxygen" data-design-system-component="Text"') #select the class under which the text element sits

    send_discord_notification("The script is running.")

    if booking_status_div and "Bitte entschuldigen Sie. Die Buchung ist leider nicht möglich." not in booking_status_div.text.lower(): #change to what the element on your target site says
        print("Booking is now possible!")
        send_discord_notification("Booking is now possible!")
        send_discord_notification(f"@{discord_user_id}")
        break
    else:
        send_discord_notification("Booking is not possible at the moment.")

    time.sleep(600)
