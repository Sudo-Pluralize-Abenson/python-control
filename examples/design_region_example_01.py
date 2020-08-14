""" 
design_region_example_01.py - using the design_region module and class

Authors: 
Rico AR Picone, 
Parth Gogate
Date (initial): 3 October 2019
"""
#importing the control to get control.design_region()
from control import design_region
from scipy import pi
#printing doc string for the class and all the methods
help(design_region)

#define pi
#pi=3.14159

#more digits of pi if needed
#3.14159265358979323846264338327950288419716939937510 

# create design_region instance
dr1 = design_region()

# r and theta test

dr1.r = [2,4]
dr1.theta = [pi/2,pi]

# plot design region
dr1.plot_dr()


############################################################
#resetting design_region for new parameters
#need to re-initialize 
dr1 = design_region()

# x and y test
dr1.x = [-1,-4]
dr1.y = [0,pi]

# plot design region
dr1.plot_dr()

