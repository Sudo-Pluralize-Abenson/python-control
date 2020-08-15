""" 
design_region_example_01.py - using the design_region module and class

Authors: 
Rico AR Picone, 
Parth Gogate
Date (initial): 3 October 2019
"""
#importing the control to get control.design_region()

# incase someone also has issue importing from control. the following code can be used instead.
# MODULE_PATH = "C:/Users/USER/Documents/GitHub/python-control/control/__init__.py"
# MODULE_NAME = "control"
# import importlib
# import sys
# spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
# module = importlib.util.module_from_spec(spec)
# sys.modules[spec.name] = module 
# spec.loader.exec_module(module)
from control import design_region


#printing doc string for the class and all the methods
#help(design_region)

#define pi
pi=3.14159

#more digits of pi if needed
#pi=3.14159265358979323846264338327950288419716939937510 

# create design_region instance
#dr1 = module.design_region()
dr1 = design_region()

# r and theta test

dr1.r = [2,4]
dr1.theta = [-2,pi]

# plot design region
dr1.plot_dr()


############################################################
#resetting design_region for new parameters
#need to re-initialize 
#dr1 = module.design_region()
dr1 = design_region()


# x and y test
dr1.x = [-1,-4]
dr1.y = [-3,pi]

# plot design region
dr1.plot_dr()

############################################################
#resetting design_region for new parameters
#need to re-initialize 
#dr1 = module.design_region()
dr1 = design_region()

# z and wn test.

dr1.z = [0.3,0.8] # must be between 0 and 1 since only underdamped systems are being analysed
dr1.wn = [0,pi] # must be positive

# plot design region
dr1.plot_dr()
