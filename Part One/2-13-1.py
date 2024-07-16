'''1. Remove the Axes (top, bottom, left, right) displayed together with the 
clock. 


2. In the sample code, the hour and minute hands only point to full hour and 
minute numbers, respectively. In other words, their positions are not 
updated following the second hand movement, which is not realistic. 
Improve the code to have the hour and minute hands to update their 
positions synchronized with the movement of the second hand. 


3. Add a fourth clock hand, called the GMT hand. The GMT hand should be 
rendered in yellow color, and it will point to the hour of the GMT time zone 
but utilize the clock face to indicate the 24 hours instead of 12 hours as in 
displaying the local time. Namely, 0 oclock GMT hour hand will point to 
the 0 degree , and 12 oclock GMT hour hand will point to the 180 degree.'''

## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np
import time

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/lenna.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
GMT_hand_length = 200
GMT_hand_width = 10
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

# Remove the axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')

while True:
    plt.imshow(background)

    # First retrieve the time
    now_time = datetime.now()
    local_hour = now_time.hour
    GMT_hour = time.gmtime()
    minute = now_time.minute
    second = now_time.second

    # Calculate end points of hour, minute, second, and GMT hands
    hour_vector = clock_hand_vector(local_hour / 12 * 2 * np.pi, hour_hand_length)
    minute_vector = clock_hand_vector(minute / 60 * 2 * np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second / 60 * 2 * np.pi, second_hand_length)
    GMT_vector = clock_hand_vector(GMT_hour / 24 * 2 * np.pi, GMT_hand_length)

    # Plotting the clock hands
    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length=3, linewidth=hour_hand_width, color='black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth=minute_hand_width, color='black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth=second_hand_width, color='red')
    plt.arrow(center[0], center[1], GMT_vector[0], GMT_vector[1], linewidth=GMT_hand_width, color='yellow')

    plt.pause(0.1)
    plt.clf()
