#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:19:06 2021

@author: z003z7n
"""

def is_a_min_heap(heap):
    
    #left child will have index 2*i + 1
    #right child will have index 2*i + 2
    #maximum index to check (i) is length of heap - 2 // 2
    
    max_index = len(heap) - 2 // 2
    
    for i in range(max_index):
        
        if heap[i] > heap[2*i + 1] or heap[i] > heap[2*i + 2]:
            return False
        
        return True
    
if __name__ == '__main__':
    
    heap = [1,2,3,4,5]
    heap2 = [1,2,3,5,4]
    heap3 = [4,6,3,2,-2]
    
    print(is_a_min_heap(heap))
    print(is_a_min_heap(heap2))
    print(is_a_min_heap(heap3))