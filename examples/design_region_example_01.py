""" design_region_example_01.py - using the design_region module and class

Authors: Rico AR Picone
Date (initial): 3 October 2019
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
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

dr1.xy_to_zw()