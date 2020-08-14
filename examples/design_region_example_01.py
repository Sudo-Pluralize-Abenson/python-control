""" design_region_example_01.py - using the design_region module and class

Authors: Rico AR Picone
Date (initial): 3 October 2019
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'../')
import control as ct

# create design_region instance
dr1 = ct.design_region()

# print attributes and defaults
help(ct.design_region())

# set and print some parameters
# r and theta test

dr1.r = [2,4]
dr1.theta = [-pi,pi]

# plot design region
dr1.plot_dr()

#resetting design_region for new parameters
#need to re-initialize 
dr1 = ct.design_region()

# x and y test
dr1.x = [-2,-4]
dr1.y = [-pi/2,pi]

# plot design region
dr1.plot_dr()
# stuff that's broken

# # projection stuff?
# # dr1.theta = [pi/2,pi] # won't plot after this because we're not properly updating dr_xy
# print(dr1.dr_xy)

# # mixing r and theta stuff
# print(dr1.dr_xy)
# print(dr1.dr_rt)
# dr1.x = [-4,-1]
# # dr1.y = [2,6]
# print(dr1.dr_xy) # updated!
# print(dr1.dr_rt) # updated!
# print(dr1.r) # updated!
# print(dr1.theta) # updated!

# # overshoot
# dr1.OS = [10,20]