from machine import Pin
from scales import Scales
from utime import sleep

# Represents a class controlling a load cell sensor with an amplifier.
class WeightCell:
    # Initialize the class.
    def __init__(self):
        data_pin = Pin(27, Pin.IN, pull=Pin.PULL_DOWN)  # Data pin for the load cell
        clock_pin = Pin(26, Pin.OUT)  # Clock pin for the load cell
        
        # Initialize the Scales object (which extends HX711)
        self.scales = Scales(data_pin, clock_pin)

        # Perform tare operation (zeroing the scale)
        self.scales.tare()

    # Get the current weight on the load cell.
    def getCurrentWeight(self):
        try:
            # Read weight value, adjust the calc accordingly
            weight = (self.scales.stable_value()*(0.0005)*8)/100

        except KeyboardInterrupt:
            print("Interrupted")

        except Exception as e:
            print("Exception during measurement:", e)

        return weight


