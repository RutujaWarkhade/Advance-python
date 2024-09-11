# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:46:17 2024

@author: OM
"""
#map function
"""
map function applies to each element in sequence
"""
#######################
lst=[34,12,63,32,67]
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)
#############################

#filter
"""
filter function filters a sequence of elements based 
on given condition
"""
num=[1,2,3,4,5,6,7,8,9,10]
#get only even numbers
even=filter(lambda x:x%2==0,num)
print(list(even))
########################

#reduce
"""
the reduce function is a higher order function 
that applies a function to a sequence and returns a 
single value. It is a part of function module in python 
and it has following syntax
"""
from functools import reduce
num=[1,2,3,4,5]
#calculate sum of all ele's in give lst
s=reduce(lambda x,y:x+y,num)
print(s)
####################################
print("Welcome to roller coaster")
height=int(input("enter your height in cm"))
if height>=120:
    print("you are egible for roller coaster")
    age=int(input("enter your age in years"))
    bill=0
    if age<12:
        print("child ticket is 5$ ")
        bill=5
        #print("pay"+bill)
    elif age>=12 and age<18:
        print("your ticket is 10$")
        bill=10
        #print("pay",bill)
    elif age>=18 and age<=55:
        print("your ticket is 20$")
        bill=20        
        want_photo=input("you want photo Y or N")
        if want_photo=='Y':
          bill+=3
          print(f"your bill is {bill} in $")
    else:
        print(f"you need to pay {bill} in $")
else:
    print("Not egible")
    
###########################
height=float(input("enter your height in m"))
weight=float(input("enter your weight in kg"))
BMI=round((weight/(height*height)),2)
if BMI>=18.5:
    print(f"you are under weight and your BMI is:{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"You are normal weight and your weight is {BMI}")
elif BMI>=25 and BMI<30:
    print(f"You are over weight and your BMI is {BMI}")
elif BMI>=30 and BMI<35:
    print(f"You are obse and your BMI is {BMI}")
elif BMI>=35:
    print(f"you are clinically obse and your BMI is:{BMI}")
else:
    print(f"you are clinically obse and your BMI is:{BMI}")
################################
#lst1=[1,2,3,4,5,6,7]
#it works for only sort input only
lst1=[1,2,2,3,4,6]
lst1.sort()
#lst.sort()
def is_dublicate(list1):
    for i in range(len(lst1)-1):
    #compare current number with next number
      if(lst1[i])==lst1[i+1]:
        return True
    return False
print(is_dublicate(lst1))  
###################################
def is_leap_year(year):
    if((year>0) and (year%100!=0) and (year%400!=0) and (year%4==0)):
      return True
    return False
print(is_leap_year(1900))

"""
def leap_year(year):
    if (year%400==0) or (year%100!=0 and year%4==0):
        return True
    return False
print(leap_year(1990))

"""

#######################
#Mario Pyramid
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()#to take new line
############################
for i in range(4):
     for j in range(i+1):
         print("#",end=" ")
     print()
#################################
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
#########################
lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("the minimum value is",min)
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("Maximum value",max)
min_max(lst)
#########################
#Palindrome

def is_palindrome(input):
    if input==" ":
        return "You entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False
print(is_palindrome("step on no pets"))
##########################
#users=["admin","employe","worker","staff"]
user=input("enter user")
#for user in users:
if user=="admin":
   print("Hello Admin")
elif user=="employe":
   print("Hello Employe")
elif user=="worker":
   print("Hello Worker")
elif user=="staff":
   print("Hello Staff")
else:
   print("Hello")
#####################################
users=["admin","employe","worker","staff"]
#user=input("enter user")
for user in users:
    if user=="admin":
        print("Hello Admin")
    elif user=="employe":
        print("Hello Employe")
    elif user=="worker":
        print("Hello Worker")
    elif user=="staff":
        print("Hello Staff")
    else:
        print("Hello")
###################
#create password
import string
#pick adjectives
adjectives=['orange','yellow','red','white','blue','pink']
#pick noun
nouns=['apple','rose','panda','ball','rutuja']
#pick words
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
#create the new secure password
password=adjectives+nouns+str(number)+special_char
print("your new password is:%s"%password)
###################################
import random
import string
print("Welcome to password picker")
while True:
    adjectives=random.choice(adjectives)
    noun=random.choice(nouns)
    noun.upper()
    number=random.randrange(0,100)
#select a special character
    special_char=random.choice(string.punctuation)
#create the new secure password
    password=adjectives+noun+str(number)+special_char
    print("your new password is:%s"%password)
    response=input("would you like generate another password?")
    if response=='n':
        break
##########################
rows=int(input("enter number of rows:"))
for i in range(rows):
    print(" "*(rows-i),"*"*(2*i+1))
for i in range(rows-2,-1,-1):
    print(" ","*"*(2*i+1))
