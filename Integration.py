from MembershipFunction import Membership_Funtion
from MembershipFunction import Function_Type
import matplotlib.pyplot as plt


class Integration_Helper():
    def Centroid(f,starting_limit,ending_limit,number_of_samples):
        area = Integration_Helper.Trapezoidal_Rule(f,starting_limit,ending_limit,number_of_samples)
        centroid = Integration_Helper.Trapezoidal_Centroid(f,starting_limit,ending_limit,number_of_samples)
        print("Delta X={0}".format(float(ending_limit - starting_limit) / number_of_samples) )
        #print("Area times X={0}".format(area_times_x) )    
        print("Area={0}".format(area) )
        print("Centroid={0}".format(centroid) )
        return centroid
    
    def Trapezoidal_Rule(f, starting_limit, ending_limit, number_of_samples):
        delta_x = float(ending_limit - starting_limit) / number_of_samples
        summ = 0.0
        summ += f.find(starting_limit)
        for i in range(1, number_of_samples):
            summ += f.find(starting_limit + i*delta_x) * 2
        summ += f.find(ending_limit)
        return (delta_x / 2)* summ
        
    def Trapezoidal_Rule_Capped(f, starting_limit, ending_limit, number_of_samples, x_cap):
        delta_x = float(ending_limit - starting_limit) / number_of_samples
        summ = 0.0
        summ += f.find_capped(x_cap,starting_limit)
        for i in range(1, number_of_samples):
            summ += f.find_capped(x_cap,starting_limit + i*delta_x)*2
        summ += f.find_capped(x_cap,ending_limit)
        return (delta_x / 2)* summ 
    
    def Sipsons_Rule(f, starting_limit, ending_limit, number_of_samples):
        delta_x = float(ending_limit - starting_limit) / number_of_samples
        summ = 0.0
        summ += f.find(starting_limit)
        for i in range(1, number_of_samples):
            if(i % 2 == 0):
                summ += f.find(starting_limit + i*delta_x)*2
            else:
                summ += f.find(starting_limit + i*delta_x)*4
        summ += f.find(ending_limit)
        return (delta_x / 3)* summ 
        
    def Sipsons_Rule_Times_X(f, starting_limit, ending_limit, number_of_samples):
        print("Starting Limit={0}".format(starting_limit))
        print("Ending Limit={0}".format(ending_limit))
        print("Samples={0}".format(number_of_samples))
        delta_x = float(ending_limit - starting_limit) / number_of_samples
        print("Delta X={0}".format(delta_x))
        summ = 0.0
        summ += (f.find(starting_limit) * starting_limit)
        print("Sum;{0}={1}".format(starting_limit,summ))
        for i in range(1, number_of_samples):
            if(i % 2 == 0):
                summ += (f.find(starting_limit + i*delta_x)*2 * i)
            else:
                summ += (f.find(starting_limit + i*delta_x)*4 * i)
                
            print("Sum{0:.2f}:i={1}={2}".format(i*delta_x,summ))
            
        summ += (f.find(ending_limit) * ending_limit)
        print("Sum;{0}={1}".format(ending_limit,summ))
        return (delta_x / 3)* float(summ) 
        
    def Trapezoidal_Centroid(f, starting_limit, ending_limit, number_of_samples):
        h = float(ending_limit - starting_limit) / number_of_samples

        centroid_times_area_sum = 0
        area_sum = 0

        x=starting_limit
        x_plus_delta_x=starting_limit + h
        while(x_plus_delta_x < ending_limit):
            #get the side values of the trapizoid
            b=f.find(x_plus_delta_x)
            a=f.find(x)
            
            if(a!=0 and b!=0):
                #Find the area and centroid
                
                area = h/2*(a+b)   
                centroid = (x_plus_delta_x-h/2)*area

                
                #Get the two needed sums
                centroid_times_area_sum += centroid
                area_sum += area
            
            #increment the current trapizoid
            x += h
            x_plus_delta_x += h
            
            
        #Centroid of x = sum(centroid(x)*A)/A
        return centroid_times_area_sum/area_sum   
        
    
    def trapizodial_centroid_of_function_list_capped(f_list, starting_limit, ending_limit, number_of_samples):
        h = float(ending_limit - starting_limit) / number_of_samples
        centroid_times_area_sum = 0
        area_sum = 0            

        #Loop over each function
        for f in f_list:
            x=starting_limit
            x_plus_delta_x=starting_limit + h
            while(x_plus_delta_x < ending_limit):
                #get the side values of the trapizoid
                b=f.find_capped(x_plus_delta_x)
                a=f.find_capped(x)
                
                if(a!=0 and b!=0):
                    #Find the area and centroid                    
                    area = h/2*(a+b)   
                    centroid = (x_plus_delta_x-h/2)*area
                        
                    #Get the two needed sums
                    centroid_times_area_sum += centroid
                    area_sum += area
                
                #increment the current trapizoid
                x += h
                x_plus_delta_x += h
                
        #Centroid of x = sum(centroid(x)*A)/A
        #print(centroid_times_area_sum,area_sum)
        return centroid_times_area_sum/area_sum 
