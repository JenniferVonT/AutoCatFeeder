from networkSettings import connect_wifi
import os
from load_env import load_env, env_vars

load_env()

# Network credentials.
SSID = env_vars.get('SSID')
PASSWORD = env_vars.get('PSW')

## Connect to the WiFi network.
connect_wifi(SSID, PASSWORD)
