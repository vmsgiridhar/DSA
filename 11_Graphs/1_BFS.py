#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:59:18 2021

@author: z003z7n
"""

# Node or Vertex
class Node:
    
    def __init__(self, name):
        # Vertex Name or identifier
        self.name = name
        # Adjacent vertices of this Vertex
        self.adjacent_vertices = []
        # if visited or not
        self.visited = False
    
def Breadth_First_Search(start):
    
    # Queue follows FIFO
    queue = [start]
    
    # We will end the iteration only when queue is empty (When all the vertices are visited)
    while queue:
        
        # pop the first vertex inserted and then append the vertices of the popped vertex
        # also set the vertex to be visited
        
        visited = queue.pop(0)
        visited.visited = True
        print('{}'.format(visited.name))
        
        # appending the adjacent_vertices to queue
        for n in visited.adjacent_vertices:
            if not n.visited:
                queue.append(n)
                
        #print('Queue is: {}'.format([i.name for i in queue]))
                
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
    Breadth_First_Search(node1)
            
    
        
        
        