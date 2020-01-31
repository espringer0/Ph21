# -*- coding: utf-8 -*-
"""
Homework 1 Assignment Part 2
Created on Wed Jan 15 21:20:56 2020

@author: Emily Springer
"""

from astropy.io.votable import parse
import matplotlib.pyplot as plt

# Get votable file
votable = parse(\
 "http://nesssi.cacr.caltech.edu/DataRelease/upload/result_web_fileUVw9H2.vot"\
                 , pedantic=False)
# Get table from the file
table = votable.get_first_table()
data = table.array
# Plot the data with error bars for y-axis
plt.errorbar(data['ObsTime'], data['Mag'], yerr = data['Magerr'], fmt='.k')
plt.xlabel('Date (MJD)') 
plt.ylabel('V mag') 
plt.title('Light Curves') 
plt.gca().invert_yaxis()
