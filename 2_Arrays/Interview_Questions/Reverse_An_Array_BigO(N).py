#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 22:05:50 2021

@author: z003z7n
"""

#way 1
import numpy as np

arr = np.random.choice(20,size=5,replace=False)

print(arr)
def reverse_an_array(arr):
    print(arr[::-1])

reverse_an_array(arr)

#way 2
for i in range(-1,-len(arr)-1,-1):
    print(arr[i])

#way 3
start_index = 0
end_index = len(arr) - 1

for i in range(len(arr)):
    print('{} start_index: {} end_index: {}'.format(i, start_index, end_index))
    if start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    # termination condition
    if start_index == end_index:
        break
print('Sorted Array: {}'.format(arr))

#way 4
def reverse(arr):
    start_index = 0
    end_index = len(arr) - 1
    
    while end_index > start_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    
    return(arr)
        
print('Sorted Array Algo with While: {}'.format(reverse(arr)))
    