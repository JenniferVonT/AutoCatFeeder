from machine import Pin, PWM # type: ignore
from utime import sleep # type: ignore

# Represents a class controlling the servo for the food dispenser valve.
class ServoClass:
    # Initialize the class.
    def __init__(self):
        self.STOP = 1500000  # Stop the motor
        self.LEFT = 1200000  # Rotate counter-clockwise
        self.RIGHT = 2000000  # Rotate clockwise

        self.pwm = PWM(Pin(15))

        self.pwm.freq(50)
        self.pwm.duty_ns(self.STOP)  # Initially stop the motor

    # Open the valve once.
    def turnValve(self):
        self.pwm.duty_ns(self.LEFT)  # Rotate counter-clockwise
        sleep(0.5)  # Adjust the time to reach approximately 11 o'clock position
        self.pwm.duty_ns(self.STOP)  # Stop the motor
        sleep(2)  # Wait for X seconds
        self.pwm.duty_ns(self.RIGHT)  # Rotate clockwise
        sleep(0.5)  # Adjust the time to reach approximately 2 o'clock position
        self.pwm.duty_ns(self.STOP)  # Stop the motor
        self.pwm.duty_ns(self.LEFT)  # Rotate counter-clockwise
        sleep(0.5)  # Adjust the time to reach approximately 11 o'clock position
        self.pwm.duty_ns(self.STOP)  # Stop the motor
        sleep(2)  # Wait for X seconds
        self.pwm.duty_ns(self.RIGHT)  # Rotate clockwise
        sleep(0.5)  # Adjust the time to reach approximately 2 o'clock position
        self.pwm.duty_ns(self.STOP)  # Stop the motor

