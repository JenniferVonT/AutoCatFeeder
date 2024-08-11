from machine import Pin # type: ignore
from hx711 import *
from math import trunc

# Represents a class controlling a load cell sensor with an amplifier.
class WeightCell:
    # Initialize the class.
    def __init__(self):
        data_pin = Pin(26)  # Data pin for the load cell
        clock_pin = Pin(27)  # Clock pin for the load cell
        
        # Initialize the hx711 object.
        self.hx = hx711(clock_pin, data_pin)

        # Power up
        self.hx.set_power(hx711.power.pwr_up)

        # Set gain and save it to the hx711
        # chip by powering down then back up
        self.hx.set_gain(hx711.gain.gain_64)
        self.hx.set_power(hx711.power.pwr_down)
        hx711.wait_power_down()
        self.hx.set_power(hx711.power.pwr_up)

        # Wait for readings to settle
        hx711.wait_settle(hx711.rate.rate_10)

    # Get the current weight on the load cell in grams (truncated, no decimals).
    def getCurrentWeight(self):
        try:
            raw_value = self.hx.get_value()
            tare_offset = -66500
            known_weight_73g = -155300
            
            scale_factor = (known_weight_73g - tare_offset) / 73

            # Calculate the weight based on calibration
            val = (raw_value - tare_offset) / scale_factor

        except KeyboardInterrupt:
            print("Interrupted")

        except Exception as e:
            print("Exception during measurement:", e)

        return trunc(val)

