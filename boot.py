from networkSettings import connect_wifi
import os
from load_env import load_env

load_env()

# Network credentials.
SSID = os.getenv('SSID')
PASSWORD = os.getenv('PSW')

## Connect to the WiFi network.
connect_wifi(SSID, PASSWORD)
