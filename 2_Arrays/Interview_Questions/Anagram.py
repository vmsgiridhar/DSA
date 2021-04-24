#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:32:26 2021

@author: z003z7n
"""

#way 1 = O(N) way.
given_string = 'restful'
target_string = 'fluster'
given_string = list(given_string)
target_string = list(target_string)
for letter in target_string:
    if letter in given_string:
        given_string.pop(given_string.index(letter))
        print(given_string)
if len(given_string) == 0:
    print('Anangram')
else:
    print('Not an Anagram')
        
    


        