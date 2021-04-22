#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 10:12:15 2021

@author: z003z7n
"""

given_number = 1234

def reverse_given_number(given_number):
    reverse_number = 0
    while(given_number > 0):
        remainder = given_number % 10
        reverse_number = reverse_number * 10 + remainder
        given_number = given_number // 10
    print(reverse_number)

reverse_given_number(given_number)