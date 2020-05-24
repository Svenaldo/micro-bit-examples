import serial
import turtle
import sys
import datetime
import time

turtle.hideturtle()
turtle.setheading(90)
turtle.width=3
turtle.dot(size=5)
turtle.bgcolor("lawngreen")
turtle.color("blue")

ser = serial.Serial('/dev/ttyACM3', 115200, timeout=1)

dircetion = 0
previous_direction = 0
deviation = 0

def print_log():
    print(timestamp + "\tdirection: " + str(direction) + "\tdeviation: " + str(deviation))

while True:
    time.sleep(1)
    try:
        timestamp = datetime.datetime.now().strftime("%x %X")
        serial_value = ser.readline().strip()
        if (serial_value <> ''):
            direction = int(serial_value)
            deviation = abs(direction - previous_direction)
            if (deviation > 180): deviation = 360 - deviation
   
            print_log()

            turtle.right(direction)
            turtle.forward(10)
            turtle.left(direction)
            previous_direction = direction

        else:
            print "."

    except ValueError:
        print sys.exc_info()

