# Calculate the volume of the cylinder.
# Convert cm³ into dm³.
# 1dm³ = 1L, 1L is 1Kg.

from math import pi

r = 2
h = 3
# def weight(r, h):
ev = (pi * (r ** 2) * h) / 10 # empty volume, converted to dm³
return round(ev, 2)
