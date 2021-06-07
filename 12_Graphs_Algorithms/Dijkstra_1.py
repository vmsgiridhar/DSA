#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:14:56 2021

@author: z003z7n
"""
# to implement heap
import heapq

# Edge defines the distance/weight between two vertices
# It will have a StartNode, EndNode

class Edge:
    
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        
# Vertex is a Node
# It has a name
# We can see if it is visited or not
# It will have a min_distance
# We will also maintain the predecessors ( the previous nodes to a particular node connects in shortest path. )
# adjacency list

class Vertex:
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent_verteces = []
        self.min_distance = float('inf')
        
    def __lt__(self, other):
        return self.min_distance < other.min_distance
    
class DijkstrasAlgorithm:
    
    def __init__(self):
        # this is a binary heap and not a fibonacci heap
        self.heap = []
        
    def calculate(self, start_vertex):
        
        # initialize the vertex
        start_vertex.min_distance = 0
        
        heapq.heappush(self.heap, start_vertex)
        
        # iterate the heap till all the elements are popped
        while self.heap:
            
            # pop the vertex with the lowest min_distance value
            actual_vertex = heapq.heappop(self.heap)
            
            if actual_vertex.visited:
                continue
            
            # we have the consider the neighbours of the vertex that is popped
            for edge in actual_vertex.adjacent_verteces:
                u = edge.start_vertex
                v = edge.target_vertex
                
                # we have to compare the distances
                new_distance = u.min_distance + edge.weight
                
                # compare new_distance with min_distance of target Vertex
                if new_distance < v.min_distance:
                    # there is a shorter path to v vertex
                    v.predecessor = u
                    v.min_distance = new_distance
                    
                    # update the Binary heap with new min_distance.
                    # Binary heaps would take O(N) to find and update the vertex
                    # We have log N to updte the Heap again. Overall it takes O(N) + O(log N) = O(N) time complexity
                    # If we use Fibonacci Heaps, it would take only O(1).
                    heapq.heappush(self.heap, v)
            
            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        
        print('Shortest path to Vertex is: {}'.format(vertex.min_distance))
        actual_vertex = vertex
        
        while actual_vertex is not None:
            print(actual_vertex.name)
            actual_vertex = actual_vertex.predecessor
            
            
# Implementaion

if __name__ == '__main__':
    
    # create the vertices
    node1 = Vertex('A')
    node2 = Vertex('B')
    node3 = Vertex('C')
    node4 = Vertex('D')
    node5 = Vertex('E')
    node6 = Vertex('F')
    node7 = Vertex('G')
    node8 = Vertex('H')
    
    # Directed edges between Vertices
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # handle the neighbors
    node1.adjacent_verteces.append(edge1)
    node1.adjacent_verteces.append(edge2)
    node1.adjacent_verteces.append(edge3)
    node2.adjacent_verteces.append(edge4)
    node2.adjacent_verteces.append(edge5)
    node2.adjacent_verteces.append(edge6)
    node8.adjacent_verteces.append(edge7)
    node8.adjacent_verteces.append(edge8)
    node5.adjacent_verteces.append(edge9)
    node5.adjacent_verteces.append(edge10)
    node5.adjacent_verteces.append(edge11)
    node6.adjacent_verteces.append(edge12)
    node6.adjacent_verteces.append(edge13)
    node3.adjacent_verteces.append(edge14)
    node3.adjacent_verteces.append(edge15)
    node4.adjacent_verteces.append(edge16)

    # we just have to run the application
    algorithm = DijkstrasAlgorithm()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node7)
    
            
        