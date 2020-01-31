"""
Homework 2 Assignment III Part 3
Created on Thu Jan 30 15:15:25 2020

@author: Emily Springer
"""

import urllib
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle


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
   # Split the array by components
   for array in dataArray:
       point = array.split(', ')
       xData.append(float(point[0]))
       yData.append(float(point[1]))
   
   
frequency, power = LombScargle(xData, yData).autopower(minimum_frequency=0, maximum_frequency=5)
plt.ylabel('Lomb-Scargle Power')
plt.xlabel('frequency')
plt.title('Lomb-Scargle Her X-1')
plt.plot(frequency, power) 

plt.show()