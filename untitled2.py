# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:17:23 2018

@author: cse19
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [221,239,245,256,269,277.5]

# In my original code I create a series and run on that, 
# so for consistency I create a series from the list.
freq_series = pd.Series.from_array(frequencies)

x_labels = [2012,2013,2014,2015,2016,2017]

# Plot the figure.
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Cement consumption in Million tonnes')
ax.set_xlabel('Financial Years')
ax.set_ylabel('Consumption')
ax.set_xticklabels(x_labels)

rects = ax.patches

# For each bar: Place a label
for rect in rects:
    # Get X and Y placement of label from rect.
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2

    # Number of points between bar and label. Change to your liking.
    space = 1
    # Vertical alignment for positive values
    #va = 'bottom'

    # If value of bar is negative: Place label below bar
    
    # Use Y value as label and format number with one decimal place
    label = "{:.1f}".format(y_value)

    # Create annotation
    plt.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(0, 0),          # Vertically shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        ha='center',
        color = 'black')               # Horizontally center label)            