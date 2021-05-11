#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:23:05 2021

@author: z003z7n
"""

#Queue follows First in first out
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    
    def __init__(self):
        self.num_of_nodes = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        
        self.num_of_nodes = self.num_of_nodes + 1
        newnode = Node(data)
        
        # enqueuing the first element
        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            curr_node = self.head 
            newnode.next = curr_node 
            curr_node.prev = newnode
            self.head = newnode
    
    def traverse(self):
        print('Traversing')
        curr_node = self.head 
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next 
    
    def size_of_queue(self):
        print('Size of Queue: {}'.format(self.num_of_nodes))
    
    def dequeue(self):
        self.num_of_nodes = self.num_of_nodes - 1
        last_ele = self.tail 
        last_but_one = last_ele.prev
        self.tail = last_but_one
        last_but_one.next = None
        
            
# Implementing
que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.traverse()
que.size_of_queue()
que.dequeue()
que.dequeue()
que.size_of_queue()
que.traverse()

        
        