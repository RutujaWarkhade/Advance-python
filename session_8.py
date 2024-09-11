# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:44:46 2024

@author: OM
"""
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
print(list_b)
#not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)
#[1,2,3,4,5]
#[-10,2,3,4,5]
##############################
#but with nested objects, modifying on level 2 or deep copy
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]] 
list_b=copy.copy(list_a)
#affects the order
list_a[0][0]=-10
print(list_a)
print(list_b)
#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[-10,2,3,4,5],[6,7,8,9,10]]
#deep copies
#full independent clones. use copy.deepcopy().
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
"""
         column
0th row [1,2,3,4,5]
1st row [6,7,8,9,10]
"""
list_b=copy.deepcopy(list_a)
#not affects the other
list_a[0][0]=-10
print(list_a)
print(list_b)
#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
####################
import pandas as pd
f1=pd.read_csv('buzzers.csv')
f1
############################
import pandas as pd
f1=pd.read_csv('C:/1-python/buzzers.csv')
f1
############################
#check for working directory
import os
with open('C:/1-python/buzzers.csv') as raw_data:
    print(raw_data.read())
#########################
#reading csv data as lists
import csv
with open('C:/1-python/buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
#reading csv data as dictionaries
import csv
with open('C:/1-python/buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
################################
#pre-requisite to decorators
def plus_one(number):
    number1=number + 1
    return number1
plus_one(5)
#############################
def plus_one(number):
    def add_one(number):
        number1=number + 1
        return number1
    result = add_one(number)
    return result
plus_one(4)
##################################
#passing function as a argument
#to other functions
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)
#############################
#function returning other functions
def hello_function():
    def say_hi():
        return "hi"
    return say_hi
hello=hello_function()
hello()
#always remember when you call hello_function()
#need for decorators
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

def cal_cube(numbers):
    start=time.time()
    result =[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution cube is {total_time}")
    return result

array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:11:29 2024

@author: Shree
"""

lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

##########################################
#list comprehension
lst=[num for num in range(0,20)]
print(lst)

##########################################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)

#########################################
#list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]

print(lst)

##########################################
lst=[f"{x}{y}"for x in range(3)for y in range(3)]
print(lst)

####################################
#dict comprehension
dict={x:x*x for x in range (3)}
print(dict)
#####################################
#Generator
#it is another way of creating iterators
#in a simple way where
#it uses the keyword "yield"
#instead  of returning it in a defined function
#generators are implemented using a function
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
    
############################################
gen=(x
     for x in range(3)
     
     )
next(gen)
next(gen)
next(gen)
#next(gen)
#############################################
#function which returns multiple values
#we can not apply yield to normal fun
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
##########################################
gen=range_even(6)
next(gen)
next(gen)
next(gen)
######################
#chaning generators(generator inside generators)
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
'''ele* appears to be a placeholder for an element
from an iterable,The asterisk (*) is likely
just a character used to represent a placeholder
 or a wildcard.
for instance,if you're iterating
over a list of elements, "ele*"
could symbolize any element in that list.
It's a generic representation
that doesn't correspond to any specific syntax 
in python or itertools.
'''

passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
###################################

num=int(input())

##########################################
########################################
#password picker
print("Welcome to password picker")
import string
#pick the adjectives
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
adjectives=['sleepy','slow','smelly','wet','fat','red','fluffy'
           ,'blue','white','proud','brave']

#pick the nouns
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer'
       ,'duck','panda']

#pick the words
import string
import random
print("Welcome to password picker")
while True:
    adjective=random.choice(adjectives)
    noun= random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjective + noun + str(number) + special_char
    for password in hide(lengths(passwords)):
        print(password)
        
##############################################################
#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1}{lst[index]}')
#########################################################
#same code can be implemented using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index}{item}')
#########################################################
#Use of zip function
name=['dada','mama','kaka']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
############################################
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
####################################################
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
#################################################
#use of all,if all the values are 
#true then it will produce output
lst=[2,3,-6,8,0]    #value must be non zero,+ve or -ve
if all(lst):
    print("all values are true")
else:
    print("There are null values")
####################################################
#Use of any
lst=[0,0,0,0,0]
if any(lst):
    print("It has some value")
else:
    print("All values are zero in the list")
#####################################################
#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
#########################
#now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
############################################
#cycle
#suppose you have repeated tasks to be done ,then you 
import itertools
instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
######################################################
#repeat()
from itertools import repeat
for msg in repeat("keep patience"):
    print(msg)
#############################################################
#Combinations
from itertools import combinations
players=['John','Jani','Janardhan']
for i in combinations(players,2):
    print(i)
#######################################################
#permutations
from itertools import permutations
players=['John','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)
##########################################################
#product()
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['Virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)
#########################################################
age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])

###########################################
'''
In python assignment statements (obj_b=obj_a)
do not create real copies.
it only creates a new variable with the same reference.
so when you want to make actual copies of mutable objects
(lists,dict)
and want to modify the copy without affecting the original,
you haVE TO CAREFUL.
for real copies we can use the copy module.
however ,for compound/nested objects(e.g.nested lists or dict)
and CUSTOM OBJECTS there is an important difference between shallow and deep copy
-shallow copies: only one level deep.It creates a new collection
 and populates it with refernces to the nested objects.
this means modifying a nested objects in the copy deeper
than objects.
-deep copies:A full independent clone .
It creates a new collection and then recursively 
polulates
 it with copies of the nested '''
 
lst=[1,2,3,4]
lst1=lst
print(lst)
print(lst1)
 
lst1[0]=20
print(lst)
print(lst1)