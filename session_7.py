# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:37:23 2024

@author: OM
"""
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)
###################
#we can write same method using list compression
#for loop right side and logic left side
lst=[num for num in range(0,20)]
print(lst)
#####################
names=["dada","mama","kaka"]
lst=[name.capitalize()for name in names]
#lst=[name.upper()for name in names]
print(lst)
#####################
l=[i for i in range(1,10)if i%2==0]
print(l)
###################################
#List compression whith if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)
####################
lst=[f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)
#dictionary compression
dict={x:x*x for x in range(3)}
print(dict)
###############################
#generator
#it is another way of creating iterators
#in a simple way where
#it uses keyword "yield"
#return will written one value
#yield will written multiple value at a time
#instead of returning it in a defined function
#generator are implemented using a function
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
######################
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)
################################
#function which return multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
##############################
#now instead of using for loop we can write our own
gen=range_even(6)
next(gen)
next(gen)
#chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
'''
"ele*" apperars to be a placeholder for an element from an
iterable. the astric(*) is likely just character used 
used to represent a placeholder or a wildcard.
for instance, if you are iterating over a list of elements,"ele*"
could symbolize any element in that list. it's a generic representation
that doesn't correspond to any specific syntax in python or itertools.
'''
passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
####################################
nouns=input("enter a nouns")
adjective=input("enter a adjective")
special_char=input("enter a special charater")
import random
noun=random.choice(nouns)
number=random.rangrange(0,50)
special_char=random.choice(string.punctuation)

