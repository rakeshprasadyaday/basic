# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 05:30:09 2018

@author: cse19
"""
import matplotlib.pyplot as plt 

# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5,6] 

# heights of bars 
height = [221,239,245,256,269,277.5] 

# labels for bars 
tick_label = [2012,2013,2014,2015,2016,2017] 

# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
		width = 0.8, color = [ 'blue']) 

# naming the x-axis 
plt.xlabel('Financial Years(2012-2017)') 
# naming the y-axis 
plt.ylabel('Consumption') 
# plot title 
plt.title('Cement Consumption in million tonnes') 

# function to show the plot 
plt.show() 
