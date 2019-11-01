#!/usr/bin/env python
# coding: utf-8

# In[6]:


name=input("Enter Name: ")
quater=input("Enter Quarter: ")
batch=input("Enter Batch: ")
city=input("Enter City: ")
uni=input("Enter University: ")
#print(name.upper())
msg="""
Name: {},
Quater: {},
Batch: {},
City: {},
University: {}
"""
message=msg.format(name.upper(),quater,batch,city.title(),uni.title())
print(message)


# In[3]:


name='Nauman khalid'
print(name.upper())


# In[4]:


name='nauman khalid'
print(name.isalpha())


# In[5]:


name='NAUMAN KHALID'
print(name.lower())


# In[13]:


name='Nauman Khalid'
print(len(name))


# In[ ]:




