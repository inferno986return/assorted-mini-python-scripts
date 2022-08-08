import math

rad = 20
area = 50

 # def circle_or_square(rad, area):
c = math.pi * (rad * 2) #circumferance
p = math.sqrt(area) * 4 #perimeter
if c > p:
    circle = True
else:
    circle = False

print(str(circle) + " , " + str(c) + " , " + str(p))
