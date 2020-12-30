#!/usr/bin/env python
# coding: utf-8

# # 1 Import the numpy package 

# In[1]:


import numpy as np


# # 2. Create a null vector of size 10

# In[2]:


null=np.zeros(10)
null


# In[4]:


null.dtype


# In[5]:


#convert float into integer datatype
null=np.zeros(10,"int64")
null


# # 3. Create a vector with values ranging from 10 to 49

# In[12]:


val=np.array(range(10,49))
val


# In[13]:


#simple array make by arange function
val=np.arange(10,49)
val


# # 4. Find the shape of previous array in question 3

# In[15]:


val.shape 


# # 5. Print the type and datatype of the previous array in question 3

# In[16]:


val.dtype


# In[21]:


type(val)


# # 6. Print the numpy version and the configuration
# 

# In[22]:


np.__version__


# In[28]:


np.__config__


# In[30]:


np.show_config()


# # 7. Print the dimension of the array in question 3

# In[47]:


#by there  no. of ending prhantics we can easily see out this is 1-D ARRAY:
val.ndim


# # 8. Create a boolean array with all the True values

# In[41]:


array=np.array(range(10,30),dtype=bool)
array


# # 9. Create a two dimensional array

# In[44]:


array1=np.arange(30).reshape(15,2)
array1 


# In[46]:


#by there no. of ending prhantics we can easily see out this is 2-D ARRAY:
array1.ndim


# # 10. Create a three dimensional array

# In[50]:


array2=np.arange(40).reshape(2,10,2)
array2 


# In[51]:


#by there no. of ending prhantics we can easily see out this is 3-D ARRAY:
array2.ndim


# # 11. Reverse a vector (first element becomes last)

# In[66]:


val[::-1]


# # 12. Create a null vector of size 10 but the fifth value which is 1
# 

# In[76]:


null=np.zeros(10,"int64")
null[5]=1
null


# # 13. Create a 3x3 identity matrix
# 

# In[78]:


np.arange(27).reshape(3,3,3)


# # 14. arr = np.array([1, 2, 3, 4, 5])
# 
#  # Convert the data type of the given array from int to float

# In[79]:


arr=np.array([1,2,3,4,5])
arr


# In[80]:


arr.dtype


# In[81]:


#convert int into float
arr=np.array([1,2,3,4,5],dtype=float)
arr


# In[82]:


#convert int into float
arr=np.array([1,2,3,4,5],"float")
arr


# # 15. 
# # arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
# # arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
# 
#  # Multiply arr1 with arr2

# In[85]:


arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
array3=arr1*arr2
array3


# # 16.
# # arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
# # arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
# # Make an array by comparing both the arrays provided above
# 

# In[93]:


arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr3=arr1=arr2
arr3


# # 17. Extract all odd numbers from arr with values(0-9)

# In[113]:


val=np.arange(10)
val[val%2==1]


# # 18. Replace all odd numbers to -1 from previous array
# 

# In[121]:


val=np.arange(10)                      #confuse
val[val%2==1]=-1
val


# In[117]:


val=np.arange(10)
val[val%2==1][::-1]


# # 19. 
# # arr = np.arange(10)
# 
#  # Replace the values of indexes 5,6,7 and 8 to 12

# In[123]:


arr=np.arange(10)
arr


# In[147]:


# replace 5,6,7 and 8 to 12
arr[5]=12
arr[6]=12
arr[7]=12
arr[8]=12
arr


# # 20. Create a 2d array with 1 on the border and 0 inside

# In[214]:


array=np.arange(20).reshape(4,5)
array[0:4]=0
array


# In[215]:


array[:,0]=1
array[:,4]=1
array


# In[216]:


array[0,:]=1
array


# In[218]:


array[3,:]=1
array


# # 21. 
#  # arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#  # Replace the value 5 to 12
# 

# In[236]:


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d


# In[237]:


arr2d[1,1]=12
arr2d


# # 22.
# # arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# # Convert all the values of 1st array to 64
# 

# In[252]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d


# In[249]:


arr3d.ndim


# In[253]:


arr3d[0,0]=64
arr3d


# # # 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
# 

# In[260]:


array=np.arange(10).reshape(2,5)
array


# In[261]:


arr=array[:1]
arr


# In[262]:


arr.flatten() # make 1 _D array  by using flatten we can use reval but it can change orginal value


# # 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
# 

# In[278]:


array=np.arange(10).reshape(2,5)
array


# In[280]:


arr1=array[1]
arr1 #one dimension no need to flatten


# # 25 :
# # Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows
# 

# In[295]:


array=np.arange(20).reshape(4,5)
array


# In[298]:


array[0:2,0:3]


# # 26:
# # Create a 10x10 array with random values and find the minimum and maximum values
# 

# In[306]:


array=np.arange(100).reshape(10,10)
array


# In[307]:


array.max()


# In[308]:


array.min()


# # 27.     
# # a = np.array([1,2,3,2,3,4,3,4,5,6]) 
# # b = np.array([7,2,10,2,7,4,9,4,9,8])
#  # Find the common items between a and b
# 
# 

# In[322]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])


# In[323]:


np.intersect1d(a,b)


# # 28 
# # 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# # b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# # Find the positions where elements of a and b match
# 

# In[327]:


np.where(a==b)


# # 29
# # names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# # Find all the values from array data where the values from array names are not equal to Will
# 

# In[338]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[names!="will"]
#genrate random value


# # # 30
# # names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
#  # Find all the values from array data where the values from array names are not equal to Will AND JOE
# 

# In[462]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
not_equal=(names!='Will')&(names!='Joe')
data[not_equal]
#genrate random value


# # 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.
# 

# In[346]:


array=np.arange(15).reshape(5,3)
array


# In[349]:


array.astype(np.float)


# 
# # 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.
# 

# In[358]:


array=np.arange(16).reshape(2,2,4)
array


# In[359]:


array.astype(np.float)


# # 33. Swap axes of the array you created in Question 32
# 

# In[367]:


array=np.arange(16).reshape(2,2,4)
array.astype(np.float)
np.swapaxes(array,0,1) #1 AXIS


# In[368]:


array=np.arange(16).reshape(2,2,4)
array.astype(np.float)
np.swapaxes(array,0,2) # 2AXIS 


# # 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0
# 

# In[377]:


array=np.arange(10)


# In[378]:


array


# In[383]:


array/18


# In[386]:


array[:]=0


# In[388]:


array


# # 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays
# 

# In[408]:


a=np.random.uniform(0,12,12)
b=np.random.uniform(0,12,12)
max(a) , max(b)


# # 36
# # names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# # Find the unique names and sort them out!

# In[413]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)


# # 37 . 
# # a = np.array([1,2,3,4,5])
#  # b = np.array([5,6,7,8,9])
# 
# ---
#  # From array a remove all items present in array b
# 

# In[414]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
np.setdiff1d(a,b)


# # 38 
# # Following is the input NumPy array delete column two and insert following new column in its place.
# 
# # sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# 
# # newColumn = numpy.array([[10,10,10]])

# In[439]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
sampleArray


# In[440]:


np.delete(sampleArray, 1 , axis=1)


# In[443]:


arrayt=np.delete(sampleArray, 1 , axis=1)
array
newColumn = np.array([[10,10,10]])
np.insert(array, 1, newColumn , axis=1)


# In[445]:


arrayt=np.delete(sampleArray, 1 , axis=1)
array
newColumn = np.array([[10,10,10]])
np.insert(array, 2, newColumn , axis=1)


# # 39
# # x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# # Find the dot product of the above two matrix

# In[448]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)


# # 40.
# # Generate a matrix of 20 random values and find its cumulative sum

# In[450]:


matrics=np.arange(20)
matrics


# In[456]:


rand=np.random.uniform(matrics)
rand


# In[458]:


np.sum(rand)

