"""design_region.py - module for defining a complex plane dominant pole design region
stuff stuff stuff. 
It is designed for use in the python-control library.
Routines in this module:
"""

"""
Authors: 
Rico AR Picone
Kelsey D. Buckles
Alec J Dryden
Kenneth S Echevaria
Akara Hay
Dane P Webb

Date (initial): 2 October 2019
"""

# external modules
import numpy as np

# variables to expose for import
__all__ = ['design_region'] 

# class definition!
class design_region():
  # class attributes go here
  def __init__(self):
    # initialize instance attibutes
    self.OS = np.nan
    self.Tr = np.nan

  # methods
  def update_attributes(attr):
    print("updating attributes after setting " + attr)
