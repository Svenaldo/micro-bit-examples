# micro:bit-examples

## 1. Log micro:bit compass to serial port via USB and trace/track position on screen with Turtle graphic

### Run on micro:bit to write compass heading to serial port to USB connection
```javascript
// Direct serial output (and input) to the USB connection
serial.redirectToUSB();

// write current compass heading to serial port (via USB connection)
serial.writeLine("" + input.compassHeading())
```

### On computer (PC/Laptop, Single Board Computer (SBC) like Raspberry, ...)

#### Test serial input on Linux
1. Identify connected serial device
```bash
dmesg | grep tty
```
2. Display serial input on device eg. ttyACM3
```bash
sudo screen /dev/ttyACM3 115200
```
end and kill screen session with `strg+a k`

#### Run compass heading logger and display tracing/tracking with Turtle graphics
```python
# Listen on serial device, eg. ttyACM3
ser = serial.Serial('/dev/ttyACM3', 115200, timeout=1)

# read serial input
ser.readline()
```


## 2.
