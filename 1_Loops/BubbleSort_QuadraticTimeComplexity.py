#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:30:02 2021

@author: z003z7n
"""

import numpy as np

arr = np.random.choice(20, size=10, replace=False)

print('Array is {}'.format(arr))
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            # sorting logic
            if arr[j] > arr[j+1]:
                #arr[j],arr[j+1] = arr[j+1], arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
            print('Array now is {}'.format(arr))
    return(arr)
            
print(bubblesort(arr))

