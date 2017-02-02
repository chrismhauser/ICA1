#============================================
# plotting in real time example

import time  # for sleeping
import random  # for generating random data
from matplotlib import pyplot as plt
from collections import deque

# create a queue of size N
size_of_queue = 25
init_queue_value = -1
data = deque([init_queue_value] * size_of_queue)

# setup the plot
# show at 0:20 on the x axis and 0:10 on y axis
ax = plt.axes(xlim=(0, 20), ylim=(0, 10))
line, = plt.plot(data)  # get handle to the "line" that we use for updating the plot

plt.ion()  # interactive plots can do not block on "show"
plt.show()  # show the plot on the screen

# do this until the queue is all filled in
for i in range(0, len(data)):
    # get a random number
    # and add number to the queue
    data.appendleft(random.randint(1, 10))
    data.pop()  # pop the last number off to keep queue size the same

    line.set_ydata(data)  # set the data
    plt.draw()  # and draw it out

    time.sleep(0.1)  # simulate some down time
    plt.pause(0.0001)  # pause so that the drawing updates

