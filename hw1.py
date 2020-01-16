# -*- coding: utf-8 -*-
"""
Homework 1 Assignment Part 1
Created on Wed Jan  8 14:15:21 2020

@author: Emily Springer
"""
import urllib
import matplotlib.pyplot as plt


url = 'http://nesssi.cacr.caltech.edu/cgi-bin/getcssconedbid_release2.cgi'
values = {'Name' : 'her x-1',
          'OUT': 'vot',
          'DB': 'photcat',
          'SHORT': 'short',
          'PLOT': 'plot'}
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   pageDecoded = the_page.decode("utf-8") 
   # Extract only data table part from string of html code
   dataString = ""
   beginning = False
   end = False
   for char in pageDecoded:
       # Data table begins with '['
       if char == '[':
           beginning = True
       if beginning:
           # Data table ends with '}' (exclusive)
           if char == '}':
               end = True
               break
           # Add everything to dataString that is between the beginning and end
           if not end:
               dataString += char
   # Make the string of the data table into an array
   dataArray = dataString.strip('[],').split('],[')
   xData = []
   yData = []
   yError = []
   # Split the array by components
   for array in dataArray:
       point = array.split(', ')
       xData.append(float(point[0]))
       yData.append(float(point[1]))
       yError.append(float(point[2]))
   # Plot the data with error bars for y-axis
   plt.errorbar(xData, yData, yerr = yError, fmt='.k')
   plt.xlabel('Date (MJD)') 
   plt.ylabel('V mag') 
   plt.title('Light Curves') 
   plt.gca().invert_yaxis()
