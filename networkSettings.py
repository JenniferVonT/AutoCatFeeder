import requests # type: ignore
import network # type: ignore
import time
import os
from load_env import load_env, env_vars

load_env()

ADAFRUIT_API_FEED = env_vars.get('ADAFRUIT_API_FEED')
ADAFRUIT_IO_KEY = env_vars.get('ADAFRUIT_IO_KEY')

# Connect to the local wifi using the env variables.
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to WiFi')
    print(wlan.ifconfig())

# Send a message through the telegram app.
def sendTelegramMessage(message):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(env_vars.get('BOT_TOKEN'))
    payload = {"chat_id": env_vars.get('CHAT_ID'), "text": message}
    
    response = requests.post(url, json=payload)
    print(response.json())

# Send data to Adafruit IO
def sendAdafruitData(data):
    url = f"https://io.adafruit.com/api/v2/{ADAFRUIT_API_FEED}"
    headers = {
        "X-AIO-Key": ADAFRUIT_IO_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "value": str(data)
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        print(response.text)
        
        if response.status_code == 200:
            print("Successfully sent data:", body)
        else:
            print ("Failed to send data to Adafruit", body)

    except Exception as e:
        print("An error occurred while sending data:", e)
