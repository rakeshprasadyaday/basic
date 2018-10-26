# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 05:33:29 2018

@author: cse19
"""




import matplotlib.pyplot as plt 
#
yaxis = [161.3, 174.3, 186.9,206.6,216.0,230.5,248.2,255.8,270.3,282.8,407.0 ] 
# x-coordinates of left sides of bars 
xaxis = [1,2,3,4,5,6,7,8,9,10,11] 

# heights of bars 


# labels for bars 
tick_label = [2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017] 

# plotting a bar chart 
plt.bar(xaxis, yaxis, tick_label = tick_label, 
		width = .7, color = ['green']) 

# naming the x-axis 
plt.xlabel('Financial Years(2007-2017)') 
# naming the y-axis 
plt.ylabel('Production') 
# plot title 
plt.title('Cement Production in Million tonnes') 

# function to show the plot 
plt.show() 
