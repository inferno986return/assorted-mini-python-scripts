# Create a program that calculates the area of a circle when a user enters the radius of a circle. The formula is a =  𝝅r2

import math

print("Enter radius:")

radius = float(input())
area = math.pi * radius ** 2

print("The area of the cicle is:", area)