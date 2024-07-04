from machine import Pin, ADC
from utime import sleep

# Represents a class that controlls the light sensor and LED that is used to control when the food runs low in the main tank.
class LightSensor:
    # Initialize the class.
    def __init__(self):
        self.LED = Pin(insert pin number, machine.Pin.OUT)
        self.sensor = ADC(insert pin number)
        
    # Activates the LED on one side of the container.
    def activateLED (self):
        self.LED.on()

    def deactivateLED (self):
        self.LED.off()
        
    # Activates the photo sensor and measures the light,
    def measureLight (self):
        self.activateLED() # Activate the LED.
        lightValue = self.sensor.read() # Read the light sensor value
        self.deactivateLED() # Deactivate the LED.
        return lightValue
