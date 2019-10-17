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

Marcelino Figueroa (RIP)

Date (initial): 2 October 2019
"""

# external modules
import numpy as np
from sympy import *
import inspect

# variables to expose for import
__all__ = ['design_region'] 

# class definition!
class design_region():

  # attribute getters and setters
  @property
  def x(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @x.setter
  def x(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def y(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @y.setter
  def y(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def r(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @r.setter
  def r(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def theta(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @theta.setter
  def theta(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def z(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @z.setter
  def z(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def wn(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @wn.setter
  def wn(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def OS(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @OS.setter
  def OS(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def Ts(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @Ts.setter
  def Ts(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def Tr(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @Tr.setter
  def Tr(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
  #
  @property
  def Tp(self):
    the_p = inspect.currentframe().f_code.co_name
    attribute = getattr(self,'_'+the_p)
    return self.attribute_getter(attribute)
  @Tp.setter
  def Tp(self,value):
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))

  def attribute_setter(self,value,attribute):
    # this gets called in every setter!
    if isinstance(value,list):
      return value # was array
    else:
      return [value,value] # make array

  def attribute_getter(self,attribute):
    if attribute[0]==attribute[1]:
      return attribute[0]
    else:
      return attribute

  # class attributes go here
  def __init__(self):
    # initialize instance attributes
    # _s versions are internal symbolic variables
    # _r versions are internal interval inequalities for
    #   each variable. These are really _projections_
    #   because they can depend on other variables. 
    # Design regions are in three coordinate systems:
    #     dr_xy: x,y
    #     dr_rt: r,theta
    #     dr_zw: z,wn
    # variables
    self.x = [-oo,oo]
    self.x_s = Symbol('x_s')
    self.x_r = self.x_s <= 0 # only stable for now
    self.y = [-oo,oo]
    self.y_s = Symbol('y_s')
    self.y_r = True
    self.r = [0,oo]
    self.r_s = Symbol('r_s')
    self.r_r = (self.r_s >= 0)
    self.theta = [0,2*pi]
    self.theta_s = Symbol('theta_s')
    self.theta_r = (self.theta_s>=pi/2)&(self.theta_s<=3*pi/2) # only stable for now
    self.z = [0,1] # let's only worry about underdamped for now
    self.z_s = Symbol('z_s')
    self.z_r = (self.z_s<=1)&(self.z_s>=0)
    self.wn = [0,oo]
    self.wn_s = Symbol('wn_s')
    self.wn_r = (self.wn_s >= 0)
    self.OS = [0,oo]
    self.OS_s = Symbol('OS_s')
    self.OS_r = self.OS_s >= 0
    self.Ts = [0,oo]
    self.Ts_s = Symbol('Ts_s')
    self.Ts_r = self.Ts_s >= 0
    self.Tr = [0,oo]
    self.Tr_s = Symbol('Tr_s')
    self.Tr_r = self.Tr_s >= 0
    self.Tp = [0,oo]
    self.Tp_s = Symbol('Tp_s')
    self.Tp_r = self.Tp_s >= 0
    # design regions
    self.dr_xy = (self.x_r)&(self.y_r)
    self.dr_rt = (self.r_r)&(self.theta_r)
    self.dr_zw = (self.z_r)&(self.wn_r)

  # methods
