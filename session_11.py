# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:00:55 2024

@author: Shree
"""

class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"play tennis")
        elif self.occupation=="actor":
            print(self.name,"shoot films")
    def speaks(self):
        print(self.name,"speaks how are you?")
        
    
tom=Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

maria=Human("maria_harapova","tennis player")
maria.do_work()
maria.speaks()
#####################################################################################
#code 2
class fruit:
    def __init__(self,n,c):
        self.name=n
        self.color=c
    def fruit_name(self):
        print("My name is ",self.name)
    def fruit_color(self):
        print("My color is ",self.color)
        
f1=fruit("Mango","Yellow")
f1.fruit_name()
f1.fruit_color()

f2=fruit("Grapes","Green")
f2.fruit_name()
f2.fruit_color()
####################################################################################
#single inheriance
class vehicle:
    def general_usage(self):
        print("general use:transporation")
class Car(vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels=4
        self.has_roof=True
    
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work,vacation with family")
       
class MotorCycle(vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheels=2
        self.has_roof=False
        
    def specific_usage(self):
        self.general_usage()
        print("specific usage: Local commutation,racing")

c=Car()
m=MotorCycle()
c.specific_usage()
m.specific_usage()
##########################################################################
#multiple inheritance
class Father:
    def skills(self):
        print("I like gardening,programming")
class Mother:
    def skills(self):
        print("I like cooking,art")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I like sports")

c=Child()
c.skills()
#########################################################################

        
 
        