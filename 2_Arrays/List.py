#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:45:37 2021

@author: z003z7n
"""
# We can store different types of items in a list
list_1 = list([1,'a','b','c','Ahmedabad',50.0])

# Indexing -- we can get any element with O(1) time complexity
print(list_1[0])

# Two dimensional array(list)
list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[0][0])

# Example - Remove duplicates in this list
list_3 = [2,3,4,5,6,3,4,5,7]

# temp list method
temp = []
for i in list_3:
    if i not in temp:
        temp.append(i)

# temp and set method
temp1 = []
for i in list_3:
    if i not in set(temp1):
        temp1.append(i)


# list comprehension
temp_ = []
[temp_.append(i) for i in list_3 if i not in temp_] 

# Testing prints
print(temp)
print(temp1)
print(temp_)
