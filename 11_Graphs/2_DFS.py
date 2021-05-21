#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 08:27:44 2021

@author: z003z7n
"""

# Node is a vertex 
class Node:
    
    def __init__(self, name):
        self.name = name
        self.adjacent_vertices = []
        self.visited = False

def Depth_First_Search(start):
    
    # We will be using a Stack to traverse nodes in BFS
    # Stack follows LIFO
    
    stack = [start]
    
    # We will process all the nodes till the stack is empty
    while(stack):
        
        # we will pop the Last element
        visited = stack.pop(-1)
        # we will set the popped element to visited
        visited.visited = True
        print('{}'.format(visited.name))
        # we will appennd the adjacent Vertices to Stack
        for n in visited.adjacent_vertices:
            if not n.visited:
                stack.append(n)

if __name__ == '__main__':
    
    # Creating the Nodes
    node1 = Node("Amsterdam")
    node2 = Node("Brussels")
    node3 = Node("Frankfurt")
    node4 = Node("Glasgow")
    node5 = Node("Cairo")
    node6 = Node("Delhi")
    node7 = Node("Heathrow")
    node8 = Node("Essen")
    
    # Supplying the adjacent nodes to Nodes or Cities
    node1.adjacent_vertices.append(node2)
    node1.adjacent_vertices.append(node3)
    node1.adjacent_vertices.append(node4)
    node2.adjacent_vertices.append(node5)
    node2.adjacent_vertices.append(node6)
    node4.adjacent_vertices.append(node7)
    node6.adjacent_vertices.append(node8)
    
    #Implementing the BFS
    Depth_First_Search(node1)
        
    