
import matplotlib.pyplot as plt
import numpy as np
import math

delta_time = 0
initial_velocity = 100
constant_gravitational_acceleration = 9.8 #constant 

def calculated_displacement_formula(initial_velocity,delta_time,constant_gravitational_acceleration):
    constant = 0.47
    atomosphere_density = 1.2
    area = 4 * math.pi * 10
    velocity = 100
    answer = 0.5*constant*atomosphere_density*area
    displacement_result = abs(initial_velocity * math.cos(math.radians(40))) * delta_time + 0.5 * (constant_gravitational_acceleration + answer)*(delta_time ** 2)
    return displacement_result

def final_velocity_formula(initial_velocity,constant_gravitational_acceleration,delta_time):
    constant = 0.47
    atomosphere_density = 1.2
    area = 4 * math.pi * 10
    velocity = 100
    answer = 0.5*constant*atomosphere_density*area
    finalVelocity_result = abs(initial_velocity * math.cos(math.radians(40))) - (constant_gravitational_acceleration + answer) * delta_time
    return finalVelocity_result

def velocity_point_list(delta_time):
    
    velocity_storage_List = list()
    while True:
        
        finalVelocity_result = final_velocity_formula(initial_velocity,constant_gravitational_acceleration,delta_time)
        velocity_storage_List.append(finalVelocity_result)
        delta_time += 1 
        if delta_time > 101:
            break
    delta_time = 0
    
    return velocity_storage_List

def displacement_point_list():
    
    final_list = velocity_point_list(delta_time)
    displacement_ball_list = list()
    for number in range(101):
        the_formula = abs(initial_velocity * math.cos(math.radians(40))) * final_list.index(final_list[number]) + 0.5 * (-9.8) * pow(final_list.index(final_list[number]),2)
        if the_formula >= 0:
            displacement_ball_list.append(the_formula)
    
    return displacement_ball_list

def max_height():
    displacementList = displacement_point_list()
    max_height = 0
    for element in displacementList:
        if element >= max_height:
            max_height = element
        else:
            break
    return max_height

def midpointMethod():
    initial_point = displacement_point_list()[0]
    ending_point = displacement_point_list()[-1]
    max_point = max_height()
    midpopint_1 = (initial_point + max_point)/2
    midpopint_2 = (ending_point + max_point)/2
    point_list = [initial_point,midpopint_1,max_point,midpopint_2,ending_point]
    return sum(point_list)
#print (velocity_point_list(delta_time)[:len(displacement_point_list())])
def Accuracy():
    velocity = 100
    theta=math.radians(40)
    gravitational_acceleration = 9.81
    true_displacement = pow(velocity,2) * math.sin(2*theta)/gravitational_acceleration
    return abs(true_displacement - midpointMethod())/true_displacement
def main():
    print(Accuracy())
    print(midpointMethod())
    plt.plot(displacement_point_list()) #this is how you plot the points in a line 
    plt.ylabel('distance')
    plt.xlabel('time')
    plt.show()
main()    