#!/usr/bin/env python
# coding: utf-8

# # FOR IMPORTING NUMPY
# import numpy as np

# In[7]:


import numpy as np
np.__version__


# In[ ]:


lis=[1,2,3,"pw"]
type(lis)


# In[ ]:


#list can store any typeof data
# numpy can store only homogenous data
#numpy store data in arry 
#array can be 2d,3d,4d,5d.... so on
#array is faster than list because list store element non continous
#but array store element continously


# In[8]:


l=[1,2,3,"pw" ,5.1]
arr=np.array(l)
arr


# In[9]:


#<u32>is unicode
type(arr)


# In[10]:


arr.ndim


# In[11]:


arr1=np.array([[1,2,3],[4,5,6]])
arr1


# In[ ]:





# In[12]:


lis=[1,2,3]
np.array(lis)


# In[13]:


arr2=np.array([[1,2,3,4],[5,6,7,8]])
arr2


# In[14]:


arr2.ndim


# In[15]:


type(arr2)


# In[16]:


lim=[1,2,3]
mat =np.matrix(l)
type(mat)
               


# In[17]:


#matix always be one dimention or 2 dimention 
np.matrix([[[1,2],[3,4],[5,6]]])


# In[18]:


mat


# In[19]:


t=([1,22,3],[4,5,6])
type(t)


# In[20]:


T=np.array(t)
T


# In[21]:


T


# In[22]:


t[0]


# In[23]:


t[[0]]


# In[24]:


a=T.copy()
a


# In[25]:


#MULTIPAL WA TO GENERATE ARRAY
import numpy as np


# In[26]:


arr1=np.fromfunction(lambda i,j:i!=j,(3,3))
arr1


# In[27]:


arr1.ndim


# arr1.shape 

# In[28]:


arr1.shape


# In[29]:


arr1.size


# In[30]:


arr2=np.fromfunction(lambda i,j:i*j,(3,3))
arr2


# In[31]:


for i in range(5):
    print(i)


# In[32]:


[i for i in range(5)]


# In[33]:


irr=[i for i in range(5)]
irr


# In[34]:


np.fromiter(irr ,float)#Create a new 1-dimensional array from an iterable object.


# In[35]:


np.fromstring('22 23 24',sep=" ")


# In[36]:


np.fromstring("22 23 24" ,sep=" ")


# In[37]:


a="ajay,bijay,sanjay"
b= a.split(',')
np.array(b)


# In[38]:


list(range(1,10))


# In[39]:


np.arange(1,10,2)


# # NUMPY ADVANCE 1

# In[ ]:


import numpy as np


# In[ ]:


aa=np.zeros(5)
aa


# In[ ]:


b=np.zeros((4,4))
b


# In[ ]:


c=np.ones((3,4))
c


# In[ ]:


d=np.twos(5)
d           #only zeros and ones are working but other are not working


# In[ ]:


np.array[2,2,2]


# In[ ]:


np.array([234])


# In[ ]:


np.array([[2,2,2],[2,2,2]])


# In[ ]:


A=np.zeros((2,3,2))


# In[ ]:


A+5


# In[ ]:


A.ndim


# In[ ]:


B=np.fromfunction(lambda i,j:i==j,(3,3))
B


# In[ ]:


B+5


# In[ ]:


np.eye(3)


# In[ ]:


np.empty(2)


# In[ ]:


np.empty((2,3))


# In[ ]:


import random


# In[ ]:


random.choice((1,2,3,4,5,6))


# In[ ]:


arr1=np.zeros((2,3,3,3))
arr1


# In[ ]:


arr2=np.fromfunction(lambda i,j:i==j,(3,4))
arr2


# In[ ]:


np.eye(2)


# In[ ]:


np.eye(3,4, dtype=int)


# In[ ]:


import random

random.choice((1,2,3,4,5,6))


# In[ ]:


random.randrange(1,12)


# In[ ]:


lis=["a","s","d","f","h"]

random.shuffle(lis)


# In[ ]:


lis


# In[ ]:


random.uniform(2,5)


# In[ ]:


i=5
while i<10:
    print (i)
    i=i+1


# In[ ]:


2+5


# In[ ]:


i=1
while i<10:
    print(i)
    


# In[ ]:





# In[ ]:




