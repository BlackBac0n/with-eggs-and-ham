# Displacement of an axial load

import numpy as np

print("How much force are you applying? (in newtons)")
P = float(input())
print("How long is your beam? (in meters)")
L = float(input())
print("What is the diameter of your beam? (in meters)")
diameter = float(input())
A = (np.pi / 4) * (diameter ** 2)
print("What is the modulus of elasticity? (in pascals)")
E = float(input())

d = P*L/(A*E)
print("Your displacement is " + str(d) + " meters.")