# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:17:10 2016
@author: 42
"""
import math
import matplotlib.pyplot as plt
from enum import Enum

class Function_Type(Enum):
    undefined = 1
    triangle = 2
    trapezoidal = 3
    gaussian = 4
    generalised_bell = 5
    sigmoid = 6
    
    
class Membership_Funtion():
    a = 0
    b = 0
    c = 0
    d = 0
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
        

    def find_capped(self,x_cap, x):
        return min([self.find(x_cap),self.find(x)])
    
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



def trapezoidal_rule(f, starting_limit, ending_limit, number_of_samples):
    h = float(ending_limit - starting_limit) / number_of_samples
    summ = 0.0
    summ += f.find(starting_limit)/2.0
    for i in range(1, number_of_samples):
        summ += f.find(starting_limit + i*h)
    summ += f.find(ending_limit)/2.0
    return summ * h
    
def trapezoidal_rule_capped(f, starting_limit, ending_limit, number_of_samples, x_cap):
    h = float(ending_limit - starting_limit) / number_of_samples
    summ = 0.0
    summ += f.find_capped(x_cap,starting_limit)/2.0
    for i in range(1, number_of_samples):
        summ += f.find_capped(x_cap,starting_limit + i*h)
    summ += f.find_capped(x_cap,ending_limit)/2.0
    return summ * h

def plot_integral_of_function():
    triangle = Membership_Funtion(Function_Type.triangle,0,5,10)
    print(trapezoidal_rule(triangle, 0, 10, 100))
    
    print(trapezoidal_rule_capped(triangle, 0, 10, 100, 4))


def test_plot_function(target, function):


    normal_list = []
    normal_list_capped = []
    x_list = [i/10 for i in range(0,1300)]
    for x in x_list: 
        normal_list.append(function.find(x))   
        normal_list_capped.append(function.find_capped(x,target)) 
        #triangle_list.append(triangle_function(x,0,5,10))
        #trapezoidal_list.append(trapezoidal_function(x,0,3,7,10))
        #gaussian_list.append(gaussian_function(x,5,1))
        #generalised_bell_list.append(generalised_bell_function(x,2,2,5))
        #sigmoid_list.append(sigmoid_function(x,1,-5))
    
    plt.scatter(x=x_list, y=normal_list, label='Triangle', color = 'blue', )
    plt.scatter(x=x_list, y=normal_list_capped, label='Triangle 2', color = 'red', )


    plt.axvline(x=target, ymin=0, ymax = 1, linewidth=2, color='black')
    plt.title('Membership Function')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend(loc='upper right')
    plt.figure()
    plt.draw()

def test_plot_list(target, function_list):


    for function in function_list:
        normal_list = []
        normal_list_capped = []
        x_list = [i/10 for i in range(0,1300)]
        for x in x_list: 
            normal_list.append(function.find(x))   
            normal_list_capped.append(function.find_capped(x,target)) 
            #triangle_list.append(triangle_function(x,0,5,10))
            #trapezoidal_list.append(trapezoidal_function(x,0,3,7,10))
            #gaussian_list.append(gaussian_function(x,5,1))
            #generalised_bell_list.append(generalised_bell_function(x,2,2,5))
            #sigmoid_list.append(sigmoid_function(x,1,-5))
        
        plt.scatter(x=x_list, y=normal_list, label='Triangle', color = 'blue', )
        plt.scatter(x=x_list, y=normal_list_capped, label='Triangle 2', color = 'red', )


    plt.axvline(x=target, ymin=0, ymax = 1, linewidth=2, color='black')
    plt.title('Membership Function')
    plt.xlabel('Input')
    plt.ylabel('Output')
    #plt.legend(loc='upper right')
    plt.figure()
    plt.draw()
    
def triangle_membership_function(value):
    return Membership_Funtion(Function_Type.triangle,
                              value-15,
                              value,
                              value+15)
                              
def trapezoidal_membership_function(value):
    return Membership_Funtion(Function_Type.trapezoidal,
                              value-15,
                              value-3,
                              value+3,
                              value+15)

def main():
    #Input Tempertures
    print("Please input the following:\nTarget Temperture:")
    target_temp = float(input().strip())
    print("Current Temperture:")
    current_temp = float(input().strip())
    
    
    #Constants
    VERY_COLD = 30
    COLD = 50
    MODERATE = 70
    WARM = 90
    VERY_WARM = 110


    plot_integral_of_function()
    
    current_triangle_temp_functions = []
    current_triangle_temp_functions.append(triangle_membership_function(VERY_COLD))
    current_triangle_temp_functions.append(triangle_membership_function(COLD))
    current_triangle_temp_functions.append(triangle_membership_function(MODERATE))
    current_triangle_temp_functions.append(triangle_membership_function(WARM))
    current_triangle_temp_functions.append(triangle_membership_function(VERY_WARM))
    
    current_trapezoidal_temp_function = []
    current_trapezoidal_temp_function.append(trapezoidal_membership_function(VERY_COLD))
    current_trapezoidal_temp_function.append(trapezoidal_membership_function(COLD))
    current_trapezoidal_temp_function.append(trapezoidal_membership_function(MODERATE))
    current_trapezoidal_temp_function.append(trapezoidal_membership_function(WARM))
    current_trapezoidal_temp_function.append(trapezoidal_membership_function(VERY_WARM))
    

    test_plot_list(target_temp,current_triangle_temp_functions)
    test_plot_list(target_temp,current_trapezoidal_temp_function)

    


if __name__ == '__main__':
    main()

