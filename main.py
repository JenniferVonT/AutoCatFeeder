from networkSettings import sendTelegramMessage
import time
import machine

# from servo import ServoClass
from weightCell import WeightCell

weight = WeightCell()
# servo = ServoClass()

weight.getCurrentWeight()
