# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 13:20:45 2025

@author: om
"""

#List compression

#1)for loop
#for loop right side and logic left side
lst = [i*i for i in range(10)]
print(lst)

names=["dada",'mama','kaka']
lst = [i.capitalize() for i in names]
print(lst)

#2)with if statement
def is_even(num):
    return num%2==0
lst = [num for num in range(1,11) if is_even(num)]
print(lst)

#Set compression

s = {i for i in range(5)}
print(s)

# Disctionary compression

dic = {i:i*i for i in range(6)}
print(dic)

