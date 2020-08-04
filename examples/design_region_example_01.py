""" design_region_example_01.py - using the design_region module and class

Authors: Rico AR Picone
Date (initial): 3 October 2019
"""

import numpy as np
from sympy import core
import matplotlib.pyplot as plt
from scipy.constants import pi
import sys
sys.path.append(".") # Adds higher directory to python modules path.
sys.path.append("..") # Adds higher directory to python modules path.import control as ct
import control as ct

# create design_region instance
dr1 = ct.design_region()

# print attributes and defaults
# print(dr1.__dict__)

# set and print some parameters
dr1.OS = 10
dr1.Tr = [1.3,1.5]
print(dr1.OS)
print(dr1.Tr)

print(dr1.dr_xy)
print(dr1.dr_rt)
dr1.x = [-4,-1]
# dr1.y = [2,6]
print(dr1.dr_xy) # updated!
print(dr1.dr_rt) # updated!
print(dr1.r) # updated!
print(dr1.theta) # updated!

print(dr1.dr_xy)

# plot design region
dr1.plot_dr()