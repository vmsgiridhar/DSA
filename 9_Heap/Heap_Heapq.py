#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:02:47 2021

@author: z003z7n
"""
import heapq

heap = [4,7,3,-1,2,1]

heapq.heapify(heap)

print(heap)

# Using heappush and heappop functions in heapq

nums = [4,7,3,-1,2,1]

heap = []

for num in nums:
    heapq.heappush(heap, num)

# we should get the sorted order - O(NLogN) time complexity
while heap:
    print(heapq.heappop(heap))