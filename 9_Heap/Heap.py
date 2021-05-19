#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:16:16 2021

@author: z003z7n
"""
# Representing Heap with a 1-D array

size_of_array = 10

# Implementing the Max Heap (Wherein the root node is the maximum of elements)

class MaxHeap:
    
    def __init__(self):
        # Actual number of elements in the Heap
        self.heap_size = 0
        # underlying list data structure
        self.heap = [0] * size_of_array
       
    #O(log N)
    def insert(self,item):
        
        if self.heap_size == size_of_array:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1
        
        # after every insertion we will need to see if the heap properties are followed
        # incase of max heap, the parent will always be greater thann children for all the nnode
        
        self.rule(self.heap_size - 1)

    def rule(self,index):
        
        # we will need to get the parent index of the items to compare and then swap.
        # we will go from the item being inserted to the root node.
        
        parent_index = (index - 1) // 2
        
        #case - if item being inserted is greater than the parent index, we need to swap
        if index > 0 and self.heap[index] > self.heap[parent_index] :
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # recursively going up till root node
            self.rule(parent_index)
            
    def get_max(self):
        return self.heap[0]
    
    def poll(self):
        
        max_item = self.get_max()
        
        # swap the root node with the last node and perform heapify
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size = self.heap_size - 1
        
        # Heapify - checkinng if heap properties are violated
        self.rule_down(0)
        
        return max_item
    
    def rule_down(self, index):
        
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        
        largest_index = index
        
        # checking if the left children to parennt is the largest
        
        if left_child_index < self.heap_size and self.heap[left_child_index] > self.heap[index]:
            largest_index = left_child_index
            
        # checking if the right child is larger than the left child: largest if the right child.
        
        if right_child_index < self.heap_size and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index
        
        # if the parent is larger than the children: it is a valid heap property, we terminate the recursive call to rule_down
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.rule_down(largest_index)
            
    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)
            
if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(32)
    heap.insert(14)
    heap.insert(10)
    heap.insert(1)
    heap.insert(24)
    heap.insert(-5)
    heap.insert(99)
    
    print(heap.heap)
    heap.heap_sort()
        
        
        
        
        