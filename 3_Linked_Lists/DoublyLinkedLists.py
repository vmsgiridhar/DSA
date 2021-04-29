#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:07:08 2021

@author: z003z7n
"""
class Node:
    
    def __init__(self, data):
        #data
        self.data = data
        #head node
        self.prev = None
        #tail node
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0
    
    def insert_at_start(self,data):
        
        #increase number of nodes
        self.numOfNodes = self.numOfNodes + 1
        
        #assigning the data to node
        newnode = Node(data)
        
        #if DoublyLinkedList is totally empty
        if self.head == None and self.tail == None:
            self.head = newnode
            self.tail = newnode
            
        
        #if DoublyLinkedList is not empty
        elif self.head is not None and self.tail is not None:
            existing_node = self.head
            newnode.next = existing_node
            existing_node.prev = newnode
            self.head = newnode
            
    
    def insert_at_end(self,data):
        pass
            
    def traverse_dll(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next
    
    def size_of_linked_list(self):
        return self.numOfNodes
            
#implementation
dll = DoublyLinkedList()
dll.insert_at_start(1)
dll.insert_at_start(2)
dll.insert_at_start(3)
print('Traversing the Doubly Linked List')
dll.traverse_dll()
print('Total items in the Doubly Linked List')   
print(dll.size_of_linked_list())
            
    
    