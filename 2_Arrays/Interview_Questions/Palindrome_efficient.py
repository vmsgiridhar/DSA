#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:26:09 2021

@author: z003z7n
"""

given_string = 'raddar'

#way 1
def palindrome_determiner(string):
    
    start_index = 0
    end_index = len(string) - 1
    
    while end_index > start_index:
        print('comparing {} with {}'.format(string[end_index], string[start_index]))
        #comparing logic
        if(string[end_index] == string[start_index]):
            #increment start_index
            start_index += 1
            
            #decremennt end_index
            end_index -= 1
        else:
            print('Not Palindrome')
            break
    if(end_index <= start_index):
        print('Palindrome')

palindrome_determiner(given_string)

#way 2
def palindrome_pythonic(string):
    if string == string[::-1]:
        return True
    else:
        return False
print('Pythonic Way')
print('Palindrome' if palindrome_pythonic(given_string) else 'Not Palindromme')
        
        
        