# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 14:51:20 2025

@author: om
"""
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[2232,2341,5674]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

##############################################
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[2321,9889,8899]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
##############################################
lst=[2,3,-6,4,5]
if all(lst):
    print("All values are true")
else:
    print("All values are NULL")
    
####################################
lst=[2,3,0,4,5]
if all(lst):
    print("All values are true")
else:
    print("All values are null")
    
####################################
lst=[0,0,-8,0,0]
if any(lst):
    print("There are some non zero value")
else:
    print("Useless")
    
#####################################
lst=[0,0,0,0,0]
if any(lst):
    print("It has some non zero value")
else:
    print("Useless")
    
#########################################

from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
###########################################

from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

############################################
import itertools
inst=("Eat","code","sleep")
for i in itertools.cycle(inst):
    print(i)
############################################

#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)

#combinations()
from itertools import combinations
players=['Jonh','Jani','Janardhan']
for i in combinations(players,2):
    print(i)

"""
difference between permutation and combinations?

"""
#permutations()
from itertools import permutations
players=['Jonh','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)

#products()
from itertools import products
team_a = ["Rohit","Pandya","Bhumrah"]
team_b = ["Virat","Manish","Sami"]
for pair in products(team_a, team_b):
    print(pair)
    
#####################################





