#I import the CSV file generated and analyze them to have a list of 1s, 2s, and 3s representing the width of the bar code's black strips
import csv

BarCodeData = []
newValue = 0
oldValue = 0
pulse_start = 0
pulse_end = 0
pulse_width = pulse_end - pulse_start
THRESHOLD_WIDTH = 0.2
THRESHOLD = 2

with open('BarCode.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    BarCodeData = []
    total_width = 0
    line_count = 0

    for row in csv_reader:
      line_count += 1
      value = int(row[1])
      timeValue = float(row[0])

      newValue = value

      if newValue == 1 and newValue != oldValue:
        pulse_start = timeValue
      elif newValue == 0 and newValue != oldValue:
        pulse_end = timeValue
        pulse_width = pulse_end - pulse_start
        pulse_value = int(pulse_width/THRESHOLD_WIDTH)
        if pulse_value == 4:
          pulse_value -=1
        BarCodeData.append(pulse_value)
      oldValue = value
            

    print(f'Processed {line_count} lines.')
    print(BarCodeData)
