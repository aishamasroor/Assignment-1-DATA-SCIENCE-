#!/usr/bin/env python
# coding: utf-8

# # question 1

# In[1]:


print("Twinkle, Twinkle, Little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


# # question 2

# In[2]:


import sys
version = sys.version
print(version )


# # question 3

# In[3]:


import datetime
now = datetime.datetime.now()
print("Current Date And Time")
print(now.strftime("%m-%d-%Y \n%H:%M:%S"))


# # question 4

# In[4]:


import math
radius = float(input("Enter the radius of the circle to calculate the area: "))
area = math.pi*radius**2
print("Area: ",round(area))


# # question 5

# In[1]:


name = str(input("Please enter your First and last name"))
reverse = name[::-1]
print(reverse)


# # question 6

# In[2]:


input_1 = input("Please enter whatever you want? ")
input_2 = input("Please enter whatever you want? ")
add = input_1 +  input_2
print(add)


# In[ ]:




