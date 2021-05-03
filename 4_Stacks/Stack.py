#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:03:24 2021

@author: z003z7n
"""

# LIFO: Last in first out: last item we insert is the first item we take out.

class Stack:
    
    def __init__(self):
        self.stack = []
        
    # insert item into the Stack
    def push(self, data):
        self.stack.append(data)
        
    # remove and return the last itme that have inserted (LIFO)
    def pop(self):
        
        if self.stack_size() < 1:
            return -1
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    # peek: returns the last item withour removing it
    def peek(self):
        return self.stack[-1]
    
    # if is_empty
    def is_empty(stack):
        return self.stack == []
    
    # stack size
    def stack_size(self):
        return len(self.stack)
    
# Implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print('Size: {}'.format(stack.stack_size()))
print('Popped item: {}'.format(stack.pop()))
print('Size: {}'.format(stack.stack_size()))
print('Peek item: {}'.format(stack.peek()))
print('Size: {}'.format(stack.stack_size()))