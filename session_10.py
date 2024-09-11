# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:11:46 2024

@author: OM
"""

try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("division perform successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be enterde")
    ################################
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("division perform successfully")
except ValueError:
    print("Only INTEGERS should be enterde")
except:
    print("OOPS...SOME EXCEPTION RAISED")

#Handling exception using try...except...else
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("division perform successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be enterde")
else:
    print("The result of division operation is ",quotient)
#here else part excecute all times when division perform succesfully

################################

try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("division perform successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be enterde")
else:
    print("The result of division operation is ",quotient)
finally:
    print("OVER AND OUT")
#here finally block can execute at any cost or it executes all time

# Classes
class Human:
    def _init_(self,n,o):
        self.name = n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == "Tennis player":
         print(self.name,"plays tennis ")
        elif self.occupation == "actor":
         print(self.name," Shoots film ")   
         
    def speaks (self):
       print(self.name," Says how are you ? ")

tom = Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

#########################
class Vehicle:
    def general_usage(self):
        print(" General use : transporation ")
        
class Car (Vehicle):
    def _init_(self):
        print("I'm car ")
        self.wheels = 4
        self.has_root = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use : commute to work, vacation with family ")
        
class Motorcycle(Vehicle):
    def _init_(self):
        print("I'm a motor cycle ")
        self.wheels = 2
        self.has_roof = False 
        
    def specific_usage(self):
        self.general_usage()
        print(" specific use : Local commutation, racing ")

c =Car()
m = Motorcycle()
c.specific_usage()
m.specific_usage()
#print(Issubclass(Car,MotorCycle))

###########################

class Father():
    def skills (self):#This is not constructor
        print("i like gardening, progaramming ")
    
class Mother ():
    def skills (self):#This is not constructor
        print ("I like cooking , art ")
        
class Child(Father,Mother):
    def skills (self):
        Father.skills(self)
        Mother.skills(self)
        print(" I like sports ")
        
c = Child()
c.skills()        

##################################### Classes
class Human:
    def _init_(self,n,o):
        self.name = n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == "Tennis player":
         print(self.name,"plays tennis ")
        elif self.occupation == "actor":
         print(self.name," Shoots film ")   
         
    def speaks (self):
       print(self.name," Says how are you ? ")

tom = Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

#########################
class Vehicle:
    def general_usage(self):
        print(" General use : transporation ")
        
class Car (Vehicle):
    def _init_(self):
        print("I'm car ")
        self.wheels = 4
        self.has_root = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use : commute to work, vacation with family ")
        
class Motorcycle(Vehicle):
    def _init_(self):
        print("I'm a motor cycle ")
        self.wheels = 2
        self.has_roof = False 
        
    def specific_usage(self):
        self.general_usage()
        print(" specific use : Local commutation, racing ")

c =Car()
m = Motorcycle()
c.specific_usage()
m.specific_usage()
#print(Issubclass(Car,MotorCycle))

###########################

class Father():
    def skills (self):#This is not constructor
        print("i like gardening, progaramming ")
    
class Mother ():
    def skills (self):#This is not constructor
        print ("I like cooking , art ")
        
class Child(Father,Mother):
    def skills (self):
        Father.skills(self)
        Mother.skills(self)
        print(" I like sports ")
        
c = Child()
c.skills()        

####################################
