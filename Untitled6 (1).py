#!/usr/bin/env python
# coding: utf-8

# In[77]:


# Question 1 


import math            # i searched about (import math) but i don't know what is this function do i hope we discuss that 

my_list = [2, 4, 6]

result = math.prod(my_list)
print(result) 


# In[78]:


# Question 2

def last(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)     #from google


my_list =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


print ("Sorted:")
print(sort(my_list))


# In[ ]:


# Question 3

dict1 = {'num1': 18, 'num2': 250, 'num3': 6}
dict2 = {'num1': 60, 'num2': 2240, 'num3': 147}
 
 

for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)


# In[ ]:


# Question 4

number = int(input())

numberDict = {}
for i in range(1, number+1):    # i had some problems in this line ,so i searsh it
    numberDict[i] = i*i

print(numberDict)


# In[85]:


# Question 5


#can't do it


# In[ ]:


# Question 6

s = input()
user_list = {}

for x in l :
    user_list.add(s)

print(s)


#worng don't know why

