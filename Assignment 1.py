#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Fibonccies Series
n=int(input())
a=0
b=1
num=0
while num <=n:
    num=a
    print(num)
    a=b
    b=num+b


# In[9]:


#Reverse of word
x=input("Write a word")
x
print("Reverse of given word is",x[::-1])


# In[10]:


#Count of even and odd numbers
x=list(input("Series of number is"))
a=0
b=0
for i in x:
    if (int(i)%2==0):
        a=a+1
    else:
        b=b+1
print("total count of event numbers are",a)
print("total count of odd numbers are",b)


# In[ ]:




