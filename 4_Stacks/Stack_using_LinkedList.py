#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:05:17 2021

@author: z003z7n
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack follows Last In First Out (LIFO)
class Stack:
    
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
        
    def push(self, data):
        
        # pushing is nothing but inserting elements into LL
        self.num_of_nodes = self.num_of_nodes + 1
        
        # creating a new node
        new_node = Node(data)
        
        # inserting new nodes
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head 
            self.head = new_node 
            
    def pop(self):
        
        first_element = self.head 
        next_element = first_element.next 
        first_element.next = None
        self.head = next_element 
        
        self.num_of_nodes = self.num_of_nodes - 1
        
    def traverse(self):
        
        curr_node = self.head 
        
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next 

# Implementing
st1 = Stack()
st1.push(1)
st1.push(2)
st1.push(3)
st1.push(4)
st1.push(5)
st1.pop()
st1.pop()
print('No of Elements in Stack: {}'.format(st1.num_of_nodes))
print('Traversing the list:')
st1.traverse()

            
            
        
        
    
        
    
        