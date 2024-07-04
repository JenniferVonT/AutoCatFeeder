from machine import Pin
from utime import sleep
from hx711 import HX711

# Represents a class controlling a load cell sensor with an amplifier.
class WeightCell:
    # Initialize the class.
    def __init__(self):
        data_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)  # Data pin for the load cell
        clock_pin = Pin(18, Pin.OUT)  # Clock pin for the load cell
        
        # Initialize the HX711
        self.hx711 = HX711(clock_pin, data_pin)
        self.hx711.tare()  # Reset the scale to zero

    # Get the current weight on the load cell.
    def getCurrentWeight(self):
        while(True):
            raw_wt = self.hx711.read()
            sf = 340/350000
            weight = raw_wt*sf # Get a scaling factor by measuring a known weight until it reads correct.
            print(f"{weight:.1f} grams", end="      \r")
            sleep(2)
