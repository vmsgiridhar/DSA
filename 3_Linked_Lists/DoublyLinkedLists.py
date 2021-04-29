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
    
    def insert(self,data):
        
        #increase number of nodes
        self.numOfNodes = self.numOfNodes + 1
        
        #assigning the data to node
        newnode = Node(data)
        
        #if DoublyLinkedList is totally empty
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        
        #there is at least 1 item in the data structure
        # we will keep inserting items at the end of the linked list
        else:
            newnode.prev = self.tail 
            self.tail.next = newnode
            self.tail = newnode
        
        # #if DoublyLinkedList is not empty
        # elif self.head is not None and self.tail is not None:
        #     existing_node = self.head
        #     newnode.next = existing_node
        #     existing_node.prev = newnode
        #     self.head = newnode
            
    
    def insert_at_end(self,data):
        #increase number of nodes
        self.numOfNodes = self.numOfNodes + 1
        
        #assigning the data to node
        newnode = Node(data)
        
        #if DoublyLinkedList is totally empty
        if self.head == None and self.tail == None:
            self.head = newnode
            self.tail = newnode
        
        #if DoublyLinkedList is not empty
        elif self.tail is not None:
            existing_node = self.tail
            existing_node.next = newnode
            newnode.prev = existing_node
            self.tail = newnode
            
    def traverse_forward_dll(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next
    
    def traverse_backward_dll(self):
        
        actual_node = self.tail
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.prev
    
    def size_of_linked_list(self):
        return self.numOfNodes
            
#implementation
dll = DoublyLinkedList()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert('A')
dll.insert(4)
dll.insert(5)
print('Traversing the Doubly Linked List')
dll.traverse_forward_dll()
print('Traversing the Doubly Linked List')
dll.traverse_backward_dll()
print('Total items in the Doubly Linked List')   
print(dll.size_of_linked_list())
            
    
    