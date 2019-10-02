"""design_region.py - module for defining a complex plane dominant pole design region
stuff stuff stuff. 
It is designed for use in the python-control library.
Routines in this module:
"""

"""
Authors: 
Rico AR Picone
Kelsey Buckles
Alec Dryden
Kenneth Echevaria
Akara Hay
Dane Webb

Date (initial): 2 October 2019
"""

# external modules
import numpy as np

# variables to expose for import
__all__ = ['design_region'] 

# class definition!
class design_region(
    OS=np.nan, # defaults
    Tr=np.nan, # defaults
):
  # class attributes go here
  def __init__(self, OS, Tr):
    # initialize instance attibutes
    self.OS = OS
    self.Tr = Tr

  # methods
  def update_attributes(attr):
    print("updating attributes after setting " + attr)