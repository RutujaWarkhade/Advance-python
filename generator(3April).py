# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 13:42:27 2025

@author: om
"""

#Generator
"""
1) it is another way of creating iterators
2) in function we take return keyword
3) in generator yield keyword use
4) yeild keyword should return multiple value at a time
"""
def my_fun(num):
    for i in range(num):
        yield i
gen = my_fun(11)
next(gen)
next(gen)
next(gen)

#next keyword is used to take value
#########################################

#zip() function

"""
zip() function combine multiple iterables 
such as list, tuple, string, dict, ect.
into single iterable of tuples.
"""
#zip() combine two list into single iterables
#ele of 1st iterable combine with 2nd iterable

name = ["rutuja", "tanuja", "yash", "sai"]
score = [120, 124, 122, 121]
res = zip(name, score)
print(list(res))

name=['dada','mama','kaka']
info=[9735,8923,9899]
for n, i in zip(name,info):
    print(n,i)
    
#This code will not display baba
name=['dada','mama','kaka','baba']
info=[2232,2341,5674]
for nm,inf in zip(name,info):
    print(nm,inf)