from networkSettings import sendTelegramMessage
from servo import ServoClass
from photoSensor import LightSensor
from weightCell import WeightCell
from utime import sleep, time

# Initialize all the classes.
light = LightSensor()
servo = ServoClass()
weight = WeightCell()

# Initialize a variable to track the last time a reminder was sent to the user using Telegram.
lastMessageTime = 0  # Initial value, representing epoch time.

# Define constants.
LOW_LIGHT_THRESHOLD = 90  # Adjust this threshold as needed, NEEDS ADJUSTING AFTER BOX IS BUILT AND DONE.
REFILL_WEIGHT_THRESHOLD = 10  # NEEDS ADJUSTING WHEN THE WEIGHT CELL IS WORKING AS INTENDED.
HOURS_TO_WAIT = 6 * 3600  # Convert hours to seconds, 3600 is seconds per hour so change the first number for the amount of hours.

while True:
    lightMeasurement = light.measureLight()
    print("Light measurement: ", lightMeasurement)
    # weightMeasurement = weight.getCurrentWeight() <------------ DE-COMMENT WHEN READY
    # Implement sending weight data to AdaFruit.IO for vizualisation <-------- DO NOT FORGET!
    # print("Weight measurement:", weightMeasurement) <---------- DE-COMMENT WHEN READY

    # Check if light is low and it's time to send a message
    if lightMeasurement < LOW_LIGHT_THRESHOLD:
        currentTime = time()

        # Check if enough time has passed since the last message was sent and if a new one should be sent or not.
        if currentTime - lastMessageTime >= HOURS_TO_WAIT:
            sendTelegramMessage("Food is running low! Please refill!")
            lastMessageTime = currentTime  # Update the last message time to delay next time it sends a message (don't spam reminders to often!)

    # Check if weight is low and trigger servo action
    ''' <------------------------------------------------------- DE-COMMENT WHEN READY
    if weightMeasurement < REFILL_WEIGHT_THRESHOLD:
        servo.turnValve()  # Fill the bowl.
    ''' # <----------------------------------------------------- DE-COMMENT WHEN READY
    sleep(5)  # Adjust how often to check (in seconds)

'''
# Debug and experiment with the weightCell, currently not working as intended.

while True:
  weightMeasurement = weight.getCurrentWeight()
  print("weight: ", weightMeasurement)
  sleep(1)

'''