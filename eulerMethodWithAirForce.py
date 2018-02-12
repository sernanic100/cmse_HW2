#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 12:47:59 2018

@author: nicolasserna
"""

import math
import matplotlib.pyplot as plt

time_range = range(66)
time = 66
theta=math.radians(40)
gravitational_acceleration = 9.81
velocity = 100
def get_points_above_ground(x_values,y_values):
    new_y_list = list()
    new_x_list = list()
    grand_list = list()
    iteration_count = 0
    for element in y_values:
        if element < 0:
            break
        else:
            new_y_list.append(element)
            
    for element in x_values:
        if len(new_x_list) == len(new_y_list):
            break
        else:
            new_x_list.append(element)
    grand_list = [new_x_list,new_y_list]
    return grand_list
#velocity = 100

    
def projectile_motion_euler(velocity,time,theta, gravitational_acceleration,airForce = 0):
    constant = 0.47
    atomosphere_density = 1.2
    area = 4 * math.pi * 10
    velocity = 100
    answer = 0.5*constant*atomosphere_density*area
    x_values = list()
    y_values = list()
    delta_seconds = 0
    while delta_seconds <= time - 1:

        x = velocity * delta_seconds * math.cos(theta)
        y = velocity * delta_seconds * math.sin(theta)- 0.5 * (gravitational_acceleration + answer) * pow(delta_seconds,2)
        x_values.append(x)
        y_values.append(y)
        delta_seconds += 1
    x_values = get_points_above_ground(x_values,y_values)[0]
    y_values = get_points_above_ground(x_values,y_values)[1]

    return([x_values,y_values])
    
def main(time, theta, gravitational_acceleration,velocity):

    x_values = projectile_motion_euler(velocity,time,theta, gravitational_acceleration,airForce = 0)[0]
    y_values = projectile_motion_euler(velocity,time,theta, gravitational_acceleration,airForce = 0)[1]
    new_list = get_points_above_ground(x_values,y_values)
    true_displacement = pow(velocity,2) * math.sin(2*theta)/gravitational_acceleration
    calculated_displacement = y_values[-1]
    accuracy = (abs(true_displacement - calculated_displacement)/true_displacement) * 100
    print("Question 1:\nHow many steps are required? 66 iterations")
    print("Accuracy: ",accuracy)
    print("I do not believe the accuracy is correct")
    #print(len(time_range),len(y_values))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel('distance')
    plt.plot(time_range[:len(y_values)],y_values)
main(time, theta, gravitational_acceleration,velocity)