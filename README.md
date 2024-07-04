# Automatic Cat Feeder - IoT

## Code
- MicroPython

## Hardware
- Raspberry Pi Pico W
- USB cable type-A to micro-B (for power and to insert the code using VSC and Pymkr.)
  
### Sense when the food amount is low in the main container:
- LED red 1500mcd
- Photoresistor CdS 4-7 kohm
  
### Sense when the food amount is low in the bowl:
- Load cell 1kg
- Load cell amplifier HX711

### Fills the bowl when food is low:
- Micro servo TS90/SG90 360° 1.2kg

## Build
- Outside box - Handmade plexiglass.
- Inner box - modified plastic food container.
- Bowl - metallic cat food bowl.

## Data handling:
- Adafruit IO;
  Used to track food consumption and visualize the data.
- Telegram API/Bot;
  Used to message me daily updates and warn when food is running low in the food container.
