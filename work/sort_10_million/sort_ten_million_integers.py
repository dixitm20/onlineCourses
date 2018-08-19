
# coding: utf-8

# In[8]:


import random


# # Define Function To Generate the Input List

# In[9]:


# function to generate a list of random integers (in the range 1 to 100) of given size.
def genRandList(size,minIntVal,maxIntVal):
    listrandom=[]
    for i in range(1,size+1):
        value=random.randint(minIntVal,maxIntVal)
        listrandom.append(value)
    return listrandom


# # Define function to sort the Input List

# In[10]:


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


# # Set parameters which control the creation of the input list

# In[11]:


# Set input list size
size=10000000
# Set minimum and maximum integer value the list can hold
minIntVal=1
maxIntVal=100


# # Generate the input List

# In[12]:


# Generate the input list of given size
inputRandomList=genRandList(size,minIntVal,maxIntVal)


# # Explore Input data

# In[29]:


# Print length of the input list
print('Length of the input random list : {}'.format(len(inputRandomList)))

# Print sample Input - BEGIN OF LIST
print('Starting 10 of input random List[{}:{}] : {}'.format(1,10,inputRandomList[1:10]))

# Print sample Input - MIDDLE OF LIST
print('Middle 10 of input random List[{}:{}] : {}'.format(size//2,(size//2 + 10),inputRandomList[size//2:(size//2 + 10)]))

# Print sample Input - END OF LIST
print('Last 10 of input random List[{}:{}] : {}'.format(size-10,size,inputRandomList[size-10:size]))


# # Sort the input data

# In[30]:


# sort the input list using the function defined above
outputSortedList=sortRandList(inputRandomList,minIntVal,maxIntVal)


# # Explore the sorted output data

# In[31]:


# Print length of the input list
print('Length of the output sorted list : {}'.format(len(outputSortedList)))

# Print sample Input - BEGIN OF LIST
print('Starting 10 of output sorted List[{}:{}] : {}'.format(1,10,outputSortedList[1:10]))

# Print sample Input - MIDDLE OF LIST
print('Middle 10 of output sorted List[{}:{}] : {}'.format(size//2,(size//2 + 10),outputSortedList[size//2:(size//2 + 10)]))

# Print sample Input - END OF LIST
print('Last 10 of output sorted List[{}:{}] : {}'.format(size-10,size,outputSortedList[size-10:size]))


# # The Time complexity of the algorithm(defined in function sortRandList) is : O(n)
# # The space complexity of the algorithm(defined in function sortRandList) is : O(n)
