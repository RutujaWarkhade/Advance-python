# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:51:10 2024

@author: OM
"""

#A python decorator is a function
#that takes in a function and
#returns it by adding some functionality
def say_hi():
    return 'hello there'
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()
#however, python provides a much easier way
#for us to to apply decorators
#we sipmply use @symbol before
#the function we'd like to decorate
########################
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def say_hi() :
    return 'hello there'      
say_hi()
@uppercase_decorator
def hii():
    return "rutuja"
hii()
#########################
#applying multiple decorator
#to a single function
#we can use multiple decorator
#to a single function. however,
#the decorators will be applied in the order 
#that we've called them
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@split_string
@uppercase_decorator
def say_hi():
    return'hello there'
say_hi()
####################
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took{total_time}mil sec")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
        return result
@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
        return result
array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)


#exception handaling

try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("division perform successfully")
except ZeroDivisionError:
    print("Oh this is divide by zero error... not allowed")
print("OUTSIDE try... except block")
#syntax error-compilition error
#symantic error-leads to programs producing unexpected output
#runtime error-most often lead to abnormal termination 
#common runtime error
   
