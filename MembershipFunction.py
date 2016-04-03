# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:19:17 2016

@author: 42
"""

import math
from enum import Enum

class Function_Type(Enum):
    undefined = 1
    square = 2
    triangle = 3
    trapezoidal = 4
    gaussian = 5
    generalised_bell = 6
    sigmoid = 7
    
    
class Membership_Funtion():
    a = 0
    b = 0
    c = 0
    d = 0
    y_cap = -1
    function_type = Function_Type.undefined
    
    def __init__(self,function_type,a,b,c=0,d=0):
        self.function_type = function_type
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def find(self,x):
        if(self.function_type == Function_Type.undefined): 
            print("Function_Type Undefined")
            return -1        
        
        if(self.function_type == Function_Type.triangle):
            return self.triangle_function(x)
        elif(self.function_type == Function_Type.square):
            return self.square_function(x)
        elif(self.function_type == Function_Type.trapezoidal):
            return self.trapezoidal_function(x)
        elif(self.function_type == Function_Type.gaussian):
            return self.gaussian_function(x)
        elif(self.function_type == Function_Type.generalised_bell):
            return self.generalised_bell_function(x)
        elif(self.function_type == Function_Type.sigmoid):
            return self.sigmoid_function(x)
        
        print("Function_Type Error")
        return -1
        
    def set_y_cap(self,y_cap):
        self.y_cap = y_cap
        

    def find_capped(self,x, x_cap=-1):
        if(x_cap==-1):
            return min([self.y_cap ,self.find(x)])
        else:
            return min([self.find(x_cap),self.find(x)])
        
    def approximate(self, y, guess_low, guess_high):     
        adv = 0 
        adv_y = 10000
        while((adv_y-y) > .1):
            adv = (guess_low+guess_high)/2
            adv_y = self.find(adv)
            if(adv_y == y):
                guess_low = adv
                guess_high = adv
            elif(adv_y > y):
                guess_low = adv
            else:
                guess_high = adv
            
        return adv
        
        
    def square_function(self, x):
        if(self.b-x > 0 and x-self.a > 0):
            return 1
        return 0
    
    def triangle_function(self, x):
        return max([min([(x-self.a)/(self.b-self.a),(self.c-x)/(self.c-self.b)]), 0])
    
    def trapezoidal_function(self, x):
        return max([min([(x-self.a)/(self.b-self.a),1,(self.d-x)/(self.d-self.c)]),0])
        
    def gaussian_function(self, x):
        return math.e**(-((1/2)*(x-self.a)/self.b)**2)
    
    def generalised_bell_function(self,x):
        return 1/(1+abs((x-self.c)/self.a)**(2*self.b))    
    
    def sigmoid_function(self,x):
        return 1/(1+math.e**(-self.a*(x+self.b)))