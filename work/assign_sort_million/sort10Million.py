# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:08:43 2018

@author: dixit
"""

import random

# Function to generate a list of random integers (in the range 1 to 100) of given size.
def genRandList(size,minIntVal,maxIntVal):
    listrandom=[]
    for i in range(1,size+1):
        value=random.randint(minIntVal,maxIntVal)
        listrandom.append(value)
    return listrandom


def sortRandList(inputRandomList,minIntVal,maxIntVal):
    # Intitialize (set initial frequency of each integer to 0) a dictionary to count occurence of each integer
    inputIntegerRangeFrequencyCtr={}
    for i in range(minIntVal,maxIntVal+1):
        inputIntegerRangeFrequencyCtr[i]=0
    
    # Loop through the input list to get count of each integer occurence
    for num in inputRandomList:
        inputIntegerRangeFrequencyCtr[num] += 1
    
    # Use the frequency to generate a sorted list
    outputSortedList=[]
    for i in range(minIntVal,maxIntVal+1):
        outputSortedList += [i]*inputIntegerRangeFrequencyCtr[i]

    return outputSortedList

# Set input list size
size=10000000
# Set minimum and maximum integer value the list can hold
minIntVal=1
maxIntVal=100

# Generate the input list of given size
inputRandomList=genRandList(size,minIntVal,maxIntVal)

outputSortedList=sortRandList(inputRandomList,minIntVal,maxIntVal)


print(len(inputRandomList))


print(len(outputSortedList))
print(outputSortedList)
    
