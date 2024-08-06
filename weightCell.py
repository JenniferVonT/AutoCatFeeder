from machine import Pin # type: ignore
from hx711 import *

# Represents a class controlling a load cell sensor with an amplifier.
class WeightCell:
    # Initialize the class.
    def __init__(self):
        data_pin = Pin(0)  # Data pin for the load cell
        clock_pin = Pin(26)  # Clock pin for the load cell
        
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

    # Get the current weight on the load cell.
    def getCurrentWeight(self):
        try:
            # Read weight value, adjust the calc accordingly
            val = (self.hx.get_value() * 0.001 + 53) * -1

        except KeyboardInterrupt:
            print("Interrupted")

        except Exception as e:
            print("Exception during measurement:", e)

        return val


