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

def test_plot_list(title, function_list, centroid=-1):
    for function in function_list:
        normal_list = []
        normal_list_capped = []
        x_list = [i/10 for i in range(0,1100)]
        for x in x_list: 
            normal_list.append(function.find(x))   
            normal_list_capped.append(function.find_capped(x)) 
            #triangle_list.append(triangle_function(x,0,5,10))
            #trapezoidal_list.append(trapezoidal_function(x,0,3,7,10))
            #gaussian_list.append(gaussian_function(x,5,1))
            #generalised_bell_list.append(generalised_bell_function(x,2,2,5))
            #sigmoid_list.append(sigmoid_function(x,1,-5))
        
        plt.scatter(x=x_list, y=normal_list, label='Triangle', color = 'blue', )
        plt.scatter(x=x_list, y=normal_list_capped, label='Triangle 2', color = 'red', )


    if(centroid != -1):
        plt.axvline(x=centroid, ymin=0, ymax = 1, linewidth=2, color='black')
    plt.title(title)
    plt.xlabel('Input')
    plt.ylabel('Output')
    #plt.legend(loc='upper right')
    plt.figure()
    plt.draw()

def fuzzy_and(value1, value2):
    return min([value1,value2])

def fuzzy_or(value1, value2):
    return max([value1,value2])
    
def fuzzy_not(value):
    return 1 - value

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

def gaussian_membership_function(value):
    return Membership_Funtion(Function_Type.gaussian,
                              value,
                              5)

def generalised_bell_membership_function(value):
    return Membership_Funtion(Function_Type.gaussian,
                              value,
                              5,
                              10)

def main():
    #Input Tempertures
    print("Input Current Temperature, Target Temperature")
    current_temp, target_temp = [float(x) for x in input().strip().split(',')]
    
    
    #Constants
    COLD = 50
    MODERATE = 70
    WARM = 90

#----------------------------------------------------------
    #Create Membership Functions for Tempertures
    cold_function = triangle_membership_function(COLD)
    moderate_function = triangle_membership_function(MODERATE)
    warm_function = triangle_membership_function(WARM)
  
    #Find percentages from the current temperture
    current_cold_precentage = cold_function.find(current_temp)
    current_moderate_precentage = moderate_function.find(current_temp)
    current_warm_precentage = warm_function.find(current_temp)
       
    #Add them to a list tbo be printed
    function_list = []
    function_list.append(cold_function)
    function_list.append(moderate_function)
    function_list.append(warm_function)

    #Add the y cap for the graph  
    cold_function.set_y_cap(current_cold_precentage)
    moderate_function.set_y_cap(current_moderate_precentage)
    warm_function.set_y_cap(current_warm_precentage)

    #Graph the fuzzification graph
    test_plot_list("Membership Function",function_list, current_temp)

#-----------------------------------------------------
    #Create Membership Functions for Tempertures
    cold_target_function = gaussian_membership_function(COLD)
    moderate_target_function = gaussian_membership_function(MODERATE)
    warm_target_function = gaussian_membership_function(WARM)
  
    #Find percentages from the current temperture
    target_cold_precentage = cold_target_function.find(target_temp)
    target_moderate_precentage = moderate_target_function.find(target_temp)
    target_warm_precentage = warm_target_function.find(target_temp)
       
    #Add them to a list tbo be printed
    function_target_list = []
    function_target_list.append(cold_target_function)
    function_target_list.append(moderate_target_function)
    function_target_list.append(warm_target_function)

    #Add the y cap for the graph  
    cold_target_function.set_y_cap(target_cold_precentage)
    moderate_target_function.set_y_cap(target_moderate_precentage)
    warm_target_function.set_y_cap(target_warm_precentage)

    #Graph the fuzzification graph
    test_plot_list("Target Temperture Membership Function",function_target_list, target_temp)
#-------------------------------------------------------


    ##Compute the fuzzy logic
    #Do Nothing
    nothing1 = fuzzy_and(current_cold_precentage,target_cold_precentage)
    nothing2 = fuzzy_and(current_moderate_precentage,target_moderate_precentage)
    nothing3 = fuzzy_and(current_warm_precentage,target_warm_precentage)
    #print(nothing1,nothing2,nothing3)
    nothing = fuzzy_or(fuzzy_or(nothing1,nothing2),nothing3)

    #Heat
    heat1 = fuzzy_and(current_cold_precentage,target_moderate_precentage)
    heat2 = fuzzy_and(current_cold_precentage,target_warm_precentage)
    heat3 = fuzzy_and(current_moderate_precentage,target_warm_precentage)

    #print(heat1,heat2,heat3)
    heat = fuzzy_or(fuzzy_or(heat1,heat2),heat3)

    #Cool    
    cool1 = fuzzy_and(current_moderate_precentage,target_cold_precentage)
    cool2 = fuzzy_and(current_warm_precentage,target_cold_precentage)
    cool3 = fuzzy_and(current_warm_precentage,target_moderate_precentage)

    #print(cool1,cool2,cool3)
    cool = fuzzy_or(fuzzy_or(cool1,cool2),cool3)
    
    print("--------Temperature--------")
    print("Heat:{0}".format(round(heat,2)))
    print("No Action:{0}".format(round(nothing,2)))
    print("Cool:{0}".format(round(cool,2)))

    heat_function = Membership_Funtion(Function_Type.triangle, 1, 2, 50)
    nothing_function = Membership_Funtion(Function_Type.triangle, 20, 50, 70)
    cool_function = Membership_Funtion(Function_Type.triangle, 50, 99, 100)
    
    #print("---")
    #print(heat_function.approximate(heat,0,50))
    #print(nothing_function.approximate(nothing,20,70))
    #print(cool_function.approximate(cool,50,100))
    
    heat_function.set_y_cap(heat)
    nothing_function.set_y_cap(nothing)
    cool_function.set_y_cap(cool)
    
    output_functions = []
    output_functions.append(heat_function)
    output_functions.append(nothing_function)
    output_functions.append(cool_function)

    test_plot_list("Output Function", output_functions)

    #test_plot_list(target_temp,current_triangle_temp_functions)
    #test_plot_list(target_temp,function_list)
    starting_limit = 0
    ending_limit = 100
    number_of_samples = 100
    centroid = Integration_Helper.trapizodial_centroid_of_function_list_capped(output_functions, starting_limit, ending_limit, number_of_samples)
    print("Centroid:{}".format(round(centroid,2)))

if __name__ == '__main__':
#    plot_integral_of_function()
    main()

