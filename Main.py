# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:17:10 2016
@author: 42
"""
import math
import matplotlib.pyplot as plt
from MembershipFunction import Membership_Funtion
from MembershipFunction import Function_Type
from Integration import Integration_Helper



def plot_integral_of_function():
    
    start =0
    end = 11
    steps = 100
    shape = Membership_Funtion(Function_Type.trapezoidal,1,3,7,11)
    centroid = Integration_Helper.Centroid(shape,start,end,steps)
    print(centroid)
    test_plot_function(centroid,shape)

def test_plot_function(target, function):


    normal_list = []
    normal_list_capped = []
    x_list = [i/10 for i in range(0,110)]
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
    plot_integral_of_function()
#    main()

