import time
import board
from analogio import AnalogIn, AnalogOut
initial = time.monotonic()
elapsedTime = 0.0
bar_code_data = []

THRESHOLD = 55000
TOTAL_RECORD_TIME = 10.0

analog_in = AnalogIn(board.A1)

#This function thresholds the values into 0s and 1s
def thresholdValue(value):
    if(value > THRESHOLD):
        return 1
    else:
        return 0

print("Start running")

#This function records the data through scanning and appending them and the time into a list
while elapsedTime < TOTAL_RECORD_TIME:
    light = analog_in.value
    recordValue = thresholdValue(light)
    current_time = time.monotonic()
    bar_code_data.append([elapsedTime, recordValue])
    print("{0}, {1}".format(elapsedTime, recordValue))

    time.sleep(0.1)
    elapsedTime += current_time - initial
    initial = current_time
