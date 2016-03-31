from MembershipFunction import Membership_Funtion
from MembershipFunction import Function_Type

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
        
        x_vals = []
        areas = []
        centroids_x = []
        centroids_y = []

        x=starting_limit
        x_plus_delta_x=starting_limit + h
        while(x_plus_delta_x < ending_limit):
            #get the side values of the trapizoid
            b=f.find(x_plus_delta_x)
            a=f.find(x)
            
            if(a!=0 and b!=0):
                #Find the area and centroid
                    #area of trapizoid = h/2*(a+b) 
                    #centroid of trapizoid = h/2 + h/6*((a-b)/(a+b))
                area = h/2*(a+b)            
                centroid_y = ((a**2)+(a*b)+(b**2))/(3*(a+b))
                centroid_x = h/3 * (2*a+b)/(a+b)
                x_vals.append(x_plus_delta_x-h/2)
                areas.append(area)
                centroids_x.append(centroid_x)
                centroids_y.append(centroid_y)
                
                #Get the two needed sums
                centroid_times_area_sum += centroid_y*area
                area_sum += area
            
            #increment the current trapizoid
            x += h
            x_plus_delta_x += h
            
            
        plt.scatter(x=x_vals, y=centroids_y, label='Centroid Y', color = 'blue', )
        plt.scatter(x=x_vals, y=centroids_x, label='Centroid X', color = 'green', )
        plt.scatter(x=x_vals, y=areas, label='area', color = 'black', )
        plt.title('Centroids')
        plt.xlabel('Input')
        plt.ylabel('Output')
        plt.legend(loc='upper right')
        plt.figure()
        plt.draw()
        
        #Centroid of x = sum(centroid(x)*A)/A
        return centroid_times_area_sum/area_sum   
        

def plot_integral_of_function():
    
    start = 0
    end = 13
    steps = 100
    shape = Membership_Funtion(Function_Type.triangle,0,5,10)
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

if __name__ == '__main__':
    plot_integral_of_function()