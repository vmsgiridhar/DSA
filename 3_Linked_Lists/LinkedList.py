#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:14:45 2021

@author: z003z7n
"""

# A node in Linked list
class Node:
    
    # init function
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        
class LinkedList:
    
    # init function
    def __init__(self):
        self.head = None
        self.numOfNode = 0
    
    # Insert functions
    def insert_start(self, data):
        
        self.numOfNode = self.numOfNode + 1
        new_node = Node(data)
        
        #if not self.head: # this turns to if true
        if self.head is None:
            self.head = new_node
    
        else:
            new_node.nextNode = self.head
            self.head = new_node
    
    def insert_end(self,data):
        
        self.numOfNode = self.numOfNode + 1
        new_node = Node(data)
        
        actual_node = self.head
        
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        
        actual_node.nextNode = new_node
        
    # size of linked list
    def size_of_linked_list(self):
        return self.numOfNode
    
    # traversing a list
    def traverse_linked_list(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

# testing - 1
ll1 = LinkedList()
ll1.insert_start(1)
ll1.insert_start(2)
ll1.insert_start(3)
ll1.insert_end(4)
ll1.traverse_linked_list()
    