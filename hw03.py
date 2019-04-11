# Micah Clarke
# ID: 1001288866

import numpy as np
import csv

# Original, uncorrupted pulses are represented here
pulse0 = np.ones( 10 )
pulse0 = pulse0/np.linalg.norm( pulse0 )
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ))
pulse1 = pulse1/np.linalg.norm( pulse1 )

# Read in values from csv file to be stored in "rawData" 
from numpy import genfromtxt
rawData = genfromtxt('data-communications.csv', delimiter = ',')

# List that will store the corresponding "1" or "0" bit values
processedSignal = []
# Counters that will slice the values (rawData) into partitions of 10
j = 0
k = 10
# Counter for determing the end of the file
i = 0

while i < (len(rawData)/10):

    s = slice(j,k,1)
    innerproduct0 = abs(np.dot(rawData[s],pulse0))
    innerproduct1 = abs(np.dot(rawData[s],pulse1))
    
    if(innerproduct0 > innerproduct1):
        processedSignal.append(0)
    else:
        processedSignal.append(1)
    
    i+= 1
    j+= 10
    k+= 10


# Counter for determing the end of the bits
i = 0
# Counters used for partitioning up the bits to be processed into ASCII values
j = 0
k = 7 
# Will display the end message to the user
message = []

while i < ((len(rawData)/10)/8):
    asciiNum = 0
    asciiNum = processedSignal[j] * 128
    asciiNum = asciiNum + processedSignal[j+1] * 64
    asciiNum = asciiNum + processedSignal[j+2] * 32
    asciiNum = asciiNum + processedSignal[j+3] * 16
    asciiNum = asciiNum + processedSignal[j+4] * 8
    asciiNum = asciiNum + processedSignal[j+5] * 4
    asciiNum = asciiNum + processedSignal[j+6] * 2
    asciiNum = asciiNum + processedSignal[j+7] * 1
    message.append((chr(asciiNum)))
    
    i+= 1
    j+= 8
    k+= 8

# Joins the individual characters together to form the message in the correct format
message = ''.join(message)
print(message)  

