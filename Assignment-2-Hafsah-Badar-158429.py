#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


# Task no 1
# create 2d array from 1,12 range 
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
x =np.arange(0,12).reshape((6,2)) 
x


# In[4]:



# Task2
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    #wrtie your code here
x = np.arange(9,36,dtype=np.float64).reshape((3,3,3))
x


# In[53]:


#task3 
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
        #wrtie your code here

x = np.arange(5,7*5+5).reshape((5,7))
x


# In[ ]:



#task4
#Swap columns 1 and 2 in the array arr.
#wrtie your code here
arr = np.arange(9).reshape(3, 3)
print("Original array:")
print(arr)
arr[:,[1, 2]] = arr[:,[2, 1]]
print("\nAfter swapping arrays:")
print(arr)


# In[ ]:


#task5
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   #wrtie your code here
z=np.arange(20).reshape(4, 5)
z


# In[6]:


print("zero matrix")
np.zeros(20).reshape(4,5)


# In[7]:



#task6
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
#wrtie your code here
arr=np.zeros(10)
arr


# In[8]:


arr[5]=10
arr[8]=20
arr


# In[9]:



#task7

#  Create an array of zeros with the same shape and type as X. Dont use reshape method
x = np.arange(4, dtype=np.int64)
#write your code here
x


# In[10]:


np.zeros(4,dtype=np.int64)


# In[11]:



#task8
# Create a new array of 2x5 uints, filled with 6.
x = np.arange(10).reshape(2,5)#write your code here
x


# In[12]:


x[0:]=6
x


# In[13]:



#task9
# Create an array of 2, 4, 6, 8, ..., 100.

a = np.arange(101)# write your code here
a


# In[14]:


a1= a[a%2 == 0]
a1


# In[15]:


#task10
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
arr=np.array([[3,3,3],[4,4,4],[5,5,5]])
brr=np.array([1,2,3])
subt=np.subtract(arr,brr)# write your code here 
subt


# In[16]:


#task11
    # Replace all odd numbers in arr with -1 without changing arr.
    
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2==1]=-1
#write your code here 
arr


# In[21]:


#task12
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
arr = np.array([1,2,3])
ans= [arr,arr*1+1]
np.hstack(ans)
#write your code here 


# In[58]:



#task13
# Set a condition which gets all items between 5 and 10 from arr.
arr = np.array([2, 6, 1, 9, 10, 3, 27])
ans = arr.sort()
#write your code here 
ans


# In[59]:


arr


# In[64]:


[arr[3],arr[4]]


# In[72]:


#task14
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
arr = np.arange(10, 34, 1) #write reshape code
ans=np.split(arr,4)
#write your code here 
ans


# In[20]:


import numpy as np


# In[21]:


#task15
    #Sort following NumPy array by the second column 
arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
ans=arr.sort() #write your code here 
ans


# In[ ]:




