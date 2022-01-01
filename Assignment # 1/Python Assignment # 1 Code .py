#!/usr/bin/env python
# coding: utf-8

# # Question # 1:

# 1. Write a Python program to print the following string in a specific format (see the
#     output).
#                  Twinkle, twinkle, little star,
#                              How I wonder what you arel
#                                         Up above the world so high,
#                                         Like a diamond in the sky.
#                   Twinkle, twinkle, little star,
#                              How I wonder what you are

# In[2]:


print("Twinkle,twinkle,little star, \n\tHow I wonder What you are !, \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.,\nTwinkle,little star,\n\tHow I Wonder what you are")


# # Question # 2:

# 2. Write a Python program to get the Python version you are using.

# In[3]:


import sys
print("python version")
print(sys.version)


# # Question # 3:

# 3. Write a Python program to display the current date and time.

# In[4]:


import datetime
Today = datetime.datetime.now()
print("The Current Date and Time is ", Today)


# # Question # 4:

# 4. Write a Python program which accepts the radius of a circle from the user and compute
#     the area.

# In[6]:


from math import pi
Radius = float(input("Enter the radius of the circle : "))
print("The area of the circle with radius: " +  str(Radius)  +  " is "  +  str(pi*Radius**2))


# # Question # 5:

# 5. Write a Python program which accepts the user's first and last name and print them in
#     reverse order with a space between them.

# In[7]:


F_name = input("Enter First Name :")
L_name = input("Enter Last Name :")
print(L_name + " " + F_name)


# # Question # 6:
# 6. Write a python program which takes two inputs from user and print them addition

# In[8]:


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c =  a + b
print("The addition of " ,a, "and ",b, " is ",  c )


# In[ ]:




