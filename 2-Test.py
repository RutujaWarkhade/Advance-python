# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:46:45 2024

@author: om
"""

"""
1. Check if email address valid or not in Python 
e.g. Input: my.ownsite@ourearth.org 
Output: Valid Email 
Input: ankitrai326.com 
Output: Invalid Email  
"""
import re
mail = input("enter mail :")
def get_pattern_match(pattern,mail):
    matches = re.findall(pattern,mail)
    if matches:
        print("valid")
    else:
        print("invalid")
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.org',mail)


"""
2. Write a Python program to find the median of below three values. 
Values: (25,55,65) 
"""
Values= [25,55,65] 
a=int(len(Values)/2)
print(Values[a])

"""
3. Write a program to create a decorator function to measure the 
execution time of a function.
"""

import time
def cal_square(numbers):
    start=time.time()
    result =[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution square is {total_time}")
    return result

array=range(1,100000)
out_square=cal_square(array)


"""
4. Write a python program that opens a file and handles a 
FileNotFoundError exception if the file does not exist. 
"""
try:
    import os
    with open("data.txt") as raw_data:
        print(raw_data.read())
except FileNotFoundError:
    print("FileNotFoundError")
    
"""
5. Write a python program to find the intersection of two given arrays 
using Lambda. 
Original arrays: 
[1, 2, 3, 5, 7, 8, 9, 10] 
[1, 2, 4, 8, 9] 
Intersection of the said arrays: [1, 2, 8, 9]
"""
a=[1, 2, 3, 5, 7, 8, 9, 10] 
b=[1, 2, 4, 8, 9] 
c=list(filter(lambda x : x in a,b))
print(c)
