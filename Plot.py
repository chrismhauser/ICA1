#============================================
# plotting in real time example

import time  # for sleeping
import random  # for generating random data
from matplotlib import pyplot as plt
from collections import deque
import serial

serial_port = serial.Serial('/dev/cu.usbmodem1422', 9600, timeout=1)
serial_port.flush()

# create a queue of size N
size_of_queue = 300
init_queue_value = -1
data = deque([init_queue_value] * size_of_queue)

# setup the plot
# show at 0:20 on the x axis and 0:10 on y axis
fig,ax = plt.subplots(1,1)
ax.set_xlim(0, 300)
ax.set_ylim(0, 255)
line, = plt.plot(data)  # get handle to the "line" that we use for updating the plot

# do this until the queue is all filled in
try:
    while True:
        # get a random number
        # and add number to the queue
        val = serial_port.read(100)
        if val:
            for value_as_int in val:
                value_as_int = ord(value_as_int)
                data.appendleft(value_as_int)
                data.pop()  # pop the last number off to keep queue size the same

        line.set_ydata(data)  # set the data
        plt.draw()  # and draw it out

        time.sleep(0.1)  # simulate some down time
        plt.pause(0.0001)
finally:
    serial_port.close()
