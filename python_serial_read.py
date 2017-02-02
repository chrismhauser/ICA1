#============================================
# Serial reading example
import serial

serial_port = serial.Serial('/dev/cu.usbmodem1422', 9600, timeout=1)
serial_port.flush()

while True:
    # default behavior is to return a string
    val = serial_port.read()
    if val:
        value_as_int = ord(val)
        print(val, type(val), value_as_int)


        #if value_as_int >= 100:
         #   break  # break from the loop

serial_port.close()