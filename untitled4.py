# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:32:07 2018

@author: cse19
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:17:23 2018

@author: cse19
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


frequencies = [161.3, 174.3, 186.9,206.6,216.0,230.5,248.2,255.8,270.3,282.8,407.0 ]


freq_series = pd.Series.from_array(frequencies)

x_labels = [2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]


plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Cement Production in Million tonnes')
ax.set_xlabel('Financial Years')
ax.set_ylabel('Production')
ax.set_xticklabels(x_labels)

rects = ax.patches


for rect in rects:
   
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2

   
    space = 1
    
    label = "{:.1f}".format(y_value)

   
    plt.annotate(
        label,                      
        (x_value, y_value),         
        xytext=(0, space),          
        textcoords="offset points", 
        ha='center')                 
