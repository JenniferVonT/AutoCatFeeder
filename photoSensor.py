from machine import Pin, ADC # type: ignore
from utime import sleep # type: ignore

class LightSensor:
    def __init__(self):
        self.LED = Pin(14, Pin.OUT)
        self.sensor = ADC(Pin(28))

    def activateLED(self):
        self.LED.on()

    def deactivateLED(self):
        self.LED.off()

    def measureLight(self):
        self.activateLED()
        lightValue = self.sensor.read_u16()  # Read the light sensor value
        sleep(2)
        self.deactivateLED()
        return lightValue