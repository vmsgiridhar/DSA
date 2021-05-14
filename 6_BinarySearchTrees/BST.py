#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:12:34 2021

@author: z003z7n
"""

class Node:
    
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        
class BST:
    #Binary Search Tree
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, self.root)
        else:
            #conditional insert
            self.insert_node(data, self.root)
    
    def insert_node(self, data, node):
        
        # go to left sub tree
        if data < node.data:
            if node.leftChild is not None:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        
        # go to right sub tree
        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)
                
    def traversal(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
    
    def traverse_in_order(self, node):
        
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        
        print('{}'.format(node.data))
        
        if node.rightChild:
            self.traverse_in_order(node.rightChild)
    
    def get_max_value(self):
        if self.root:
            self.get_max(self.root)
    
    def get_max(self, node):
        if node.rightChild is not None:
            return self.get_max(node.rightChild)
        return node.data
    
    def get_min_value(self):
        if self.root:
            self.get_min(self.root)
    
    def get_min(self, node):
        if node.leftChild is not None:
            return self.get_min(node.leftChild)
        return node.data
        
    

# Implementation:
tree = BST()
tree.insert(32)
tree.insert(10)
tree.insert(55)
tree.insert(1)
tree.insert(19)
tree.insert(79)
tree.insert(16)
tree.insert(23)
tree.insert(500)

print('Traversal')

tree.traversal()

print('Max')
print(tree.get_max(tree.root))

print('Min')
print(tree.get_min(tree.root))


        
    