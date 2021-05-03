#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:56:20 2021

@author: z003z7n
"""

class Queue:
    
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []
    
    #this operation has O(1) running time.
    def enqueue(self, data):
        self.queue.append(data)
    
    # O(N) linear runing time. How to solve this problem? Doubly Linked List
    # Using Doubly Linked List, we can reduce the time complexity of enqueue and dequeue to O(1)
    # We can't solve the problem using simple Linked List because, while enqueuing we will need to find the last item to add a new item, which take O(N)
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1
    
    #O(1) cconstant runninng time
    def peek(self):
        return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)
    
# implementation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print('Size: {}'.format(queue.size_queue()))
print('Dequeue: {}'.format(queue.dequeue()))
print('Size: {}'.format(queue.size_queue()))
print('Peek item: {}'.format(queue.peek()))
print('Size: {}'.format(queue.size_queue()))