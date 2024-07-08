# Run "mip.install("requests") first"
import requests
import network
import time
import os
from load_env import load_env, env_vars

load_env()

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
