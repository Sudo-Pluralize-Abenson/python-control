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
from scipy.optimize import minimize
import warnings
import sys

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
    # update self.x
    the_p = inspect.currentframe().f_code.co_name
    exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
    
    # Converts a numerical based input into the symbolic expression
    minval = self.x[0]
    maxval = self.x[1]
    x_expr = ((self.x_s >= minval) & (self.x_s <= maxval))
    self.xy_based(x_expr)
    
    if not self.is_calling_method_init():
      # x to dr_xy
      self.dr_xy = self.dr_xy & self.x_r
      if not self.is_calling_method_setter():
        # avoids loops
        # dr_xy to other drs
        self.xy_to_rt()
        self.xy_to_zw()
        # interval maps
        self.in_xy_to_rt(is_x=True)
        # TODO ...
    else:
      self.dr_xy = self.x_r
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
    
    minval = self.y[0]
    maxval = self.y[1]
    y_expr = ((self.y_s >= minval) & (self.y_s <= maxval))
    self.xy_based(y_expr)
    
    if not self.is_calling_method_init():
      # y to dr_xy
      self.dr_xy = self.dr_xy & self.y_r
      if not self.is_calling_method_setter():
        # avoids loops
        # dr_xy to other drs
        self.xy_to_rt()
        self.xy_to_zw()
        # interval maps
        self.in_xy_to_rt(is_x=False)
        # TODO
    else:
      self.dr_xy = self.dr_xy & self.x_r # region exists because x is __init__ialized first
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
    
    minval = self.r[0]
    maxval = self.r[1]
    r_expr = ((self.r_s >= minval) & (self.r_s <= maxval))
    self.rt_based(r_expr)
    
    if not self.is_calling_method_init():
      # r to dr_rt
      self.dr_rt = self.dr_rt & self.r_r
      if not self.is_calling_method_setter():
        print('... r to other stuff')
        # avoids loops
        # dr_rt to other drs
        self.rt_to_xy()
        self.rt_to_zw()
        # interval maps
        self.in_rt_to_xy()
        # TODO
    else:
      print(f"dr_rt: {self.r_r}")
      self.dr_rt = self.r_r
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
    
    minval = self.theta[0]
    maxval = self.theta[1]
    theta_expr = ((self.theta_s >= minval) & (self.theta_s <= maxval))
    self.rt_based(theta_expr)
    
    if not self.is_calling_method_init():
      # r to dr_rt
      self.dr_rt = self.dr_rt & self.theta_r
      if not self.is_calling_method_setter():
        # avoids loops
        # dr_rt to other drs
        self.rt_to_xy()
        self.rt_to_zw()
        # interval maps
        self.in_rt_to_xy()
      # TODO
    else:
      self.dr_rt = self.dr_rt & self.theta_r # region exists because x is __init__ialized first

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
    
    minval = self.z[0]
    maxval = self.z[1]
    z_expr = ((self.z_s >= minval) & (self.z_s <= maxval))
    self.zw_based(z_expr)
    
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
    
    minval = self.wn[0]
    maxval = self.wn[1]
    wn_expr = ((self.wn_s >= minval) & (self.wn_s <= maxval))
    self.zw_based(wn_expr)
    
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
    
    minval = self.OS[0]
    maxval = self.OS[1]
    OS_expr = ((self.OS_s >= minval) & (self.OS_s <= maxval))
    self.OS_based(OS_expr)
    
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
    
    minval = self.Ts[0]
    maxval = self.Ts[1]
    Ts_expr = ((self.Ts_s >= minval) & (self.Ts_s <= maxval))
    self.Ts_based(Ts_expr)
    
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
    
    minval = self.Tp[0]
    maxval = self.Tp[1]
    Tp_expr = ((self.Tp_s >= minval) & (self.Tp_s <= maxval))
    self.Tp_based(Tp_expr

  def attribute_setter(self,value,attribute):
    # this gets called in every setter!
    # pack into array if needed
    if not isinstance(value,list):
      value = [value,value] # make array
    # update corresponding variable inequality
    if not hasattr(self,f"{attribute}_r"):
      exec(f"self.{attribute}_r = (self.{attribute}_s >= {value[0]}) & (self.{attribute}_s <= {value[1]})")
    else:
      exec(f"interval = self.{attribute}_r & (self.{attribute}_s >= {value[0]}) & (self.{attribute}_s <= {value[1]})")
      exec(f"interval = interval.as_set().as_relational(self.{attribute}_s)")
      exec(f"self.{attribute}_r = interval")
    return value

  def attribute_getter(self,attribute):
    if attribute[0]==attribute[1]:
      return attribute[0]
    else:
      return attribute

  def is_calling_method_init(self):
    return inspect.stack()[2].function == '__init__'

  def is_calling_method_setter(self):
    # checks to see if this is part of a different interval setter call
    try: # stack is shorter when not a different interval setter, but I don't want to trust this completely
      calling_method = inspect.stack()[3].function
      # still text is_setter because paranoid
    except:
      calling_method = inspect.stack()[2].function
    is_setter = calling_method in ['x','y','r','theta','z','w','OS','Ts','Tr','Tp']
    return is_setter

  # class attributes go here
  def __init__(self):
    # initialize instance attributes
    # _s versions are internal symbolic variables
    # _r versions are internal interval inequalities for
    #   each variable. These are really _projections_
    #   because they can depend on other variables.
    # variables
    self.x_s = Symbol('x_s',real=True)
    self.x = [-oo,oo]
    self.y_s = Symbol('y_s',real=True)
    self.y = [-oo,oo]
    self.r_s = Symbol('r_s',real=True)
    self.r = [0,oo]
    self.theta_s = Symbol('theta_s',real=True)
    self.theta = [pi/2,pi]
    self.z_s = Symbol('z_s',real=True)
    self.z = [0,1] # let's only worry about underdamped for now
    self.wn_s = Symbol('wn_s',real=True)
    self.wn = [0,oo]
    self.OS_s = Symbol('OS_s',real=True)
    self.OS = [0,oo]
    self.Ts_s = Symbol('Ts_s',real=True)
    self.Ts = [0,oo]
    self.Tr_s = Symbol('Tr_s',real=True)
    self.Tr = [0,oo]
    self.Tp_s = Symbol('Tp_s',real=True)
    self.Tp = [0,oo]
    # design regions 
    # design regions are in three coordinate systems:
    #     dr_xy: x,y
    #     dr_rt: r,theta
    #     dr_zw: z,wn
    self.dr_xy = (self.x_r)&(self.y_r)
    self.dr_rt = (self.r_r)&(self.theta_r)
    self.dr_zw = (self.z_r)&(self.wn_r)

  # methods
  ## design region maps
  def zw_to_rt(self):
    r = self.r_s
    theta = self.theta_s
    z = self.z_s
    wn = self.wn_s
    self.dr_rt = self.dr_zw.subs(
      {wn: r,
       z: cos(pi-theta)}
    )
    return self.dr_rt

  def rt_to_zw(self):
    r = self.r_s
    theta = self.theta_s
    z = self.z_s
    wn = self.wn_s
    self.dr_zw = self.dr_rt.subs(
      {r: wn,
       theta: pi - acos(z)}
    )
    return self.dr_zw

  def rt_to_xy(self):
    x = self.x_s
    y = self.y_s
    r = self.r_s
    theta = self.theta_s
    self.dr_xy = self.dr_rt.subs(
      {r: sqrt(x**2+y**2),
       theta: atan2(y,x)}
    )
    return self.dr_xy

  def xy_to_rt(self):
    x = self.x_s
    y = self.y_s
    r = self.r_s
    theta = self.theta_s
    self.dr_rt = self.dr_xy.subs(
      {x: r*cos(theta),
       y: r*sin(theta)}
    )
    return self.dr_rt

  def zw_to_xy(self):
    x = self.x_s
    y = self.y_s
    r = self.r_s
    theta = self.theta_s
    z = self.z_s
    wn = self.wn_s
    self.dr_xy = self.dr_zw.subs(
      {wn: r,
       z: cos(pi-theta)}
    ).subs(
      {r: sqrt(x**2+y**2),
       theta: atan2(y,x)}
    )
    return self.dr_xy

  def xy_to_zw(self):
    x = self.x_s
    y = self.y_s
    r = self.r_s
    theta = self.theta_s
    z = self.z_s
    wn = self.wn_s
    self.dr_zw = self.dr_xy.subs(
      {x: r*cos(theta),
       y: r*sin(theta)}
    ).subs(
      {r: sqrt(x**2+y**2),
       theta: atan2(y,x)}
    ).subs(
      {r: wn,
       theta: pi - acos(z)}
    )
    return self.dr_zw

  ## general coordinate transformations

  def co_xy_to_rt(self,x,y):
    r = sqrt(x**2+y**2)
    t = atan2(y,x)
    return r,t

  def co_rt_to_xy(self,r,t):
    x = r*cos(t)
    y = r*sin(t)
    return x,y

  def co_zw_to_rt(self,z,w):
    r = w
    t = pi - acos(z)
    return r,t

  def co_rt_to_zw(self,r,t):
    w = r
    z = cos(pi-t)
    return z,w

  def co_xy_to_zw(self,x,y):
    r,t = self.co_xy_to_rt(x,y)
    z,w = self.co_rt_to_zw(r,t)
    return z,w

  def co_zw_to_xy(self,z,w):
    r,t = self.co_zw_to_rt(z,w)
    x,y = self.co_rt_to_xy(r,t)
    return x,y

  ## interval maps

  def in_xy_to_rt(self,is_x):
    if is_x:
      r_min,_ = self.co_xy_to_rt(min(np.abs(self.x)),0)
    else: # is_y
      r_min,_ = self.co_xy_to_rt(0,min(np.abs(self.y)))
    r_max = oo
    self.r_r = self.r_r & (self.r_s >= r_min) & (self.r_s <= r_max)
    self.r_r = self.r_r.as_set().as_relational(self.r_s) # simplify
    if (r_min != self.r[0]) or (r_max != self.r[1]):
      print('Warning: a previous assignment was more restricted and will be observed.')
    self.r = [self.r_r.as_set().start,self.r_r.as_set().end]

  def in_rt_to_xy(self):
    i_theta_pi = np.argmin(np.pi-np.array(self.theta))
    theta_pi = self.theta[i_theta_pi] # closest to pi
    theta_other = self.theta[not i_theta_pi] # further
    x_min = self.r[1]*cos(theta_pi)
    x_max = self.r[0]*cos(theta_other)
    y_min = self.r[0]*sin(theta_pi)
    y_max = self.r[1]*sin(theta_other)
    self.x_r = self.x_r & (self.x_s >= x_min) & (self.x_s <= x_max)
    self.x_r = self.x_r.as_set().as_relational(self.x_s)
    if (x_min != self.x[0]) or (x_max != self.x[1]):
      print('Warning: a previous assignment was more restricted and will be observed.')
    self.x = [self.x_r.as_set().start,self.x_r.as_set().end]
    self.y_r = self.y_r & (self.y_s >= y_min) & (self.y_s <= y_max)
    self.y_r = self.y_r.as_set().as_relational(self.y_s)
    if (y_min != self.y[0]) or (y_max != self.y[1]):
      print('Warning: a previous assignment was more restricted and will be observed.')
    self.y = [self.y_r.as_set().start,self.y_r.as_set().end]

  ## design region projections to their coordinates
  
  def xy_projector(self):
    # project dr_xy onto x and y
    var('x',real=True)
    var('y',real=True)
    if self.y_s in self.dr_xy.free_symbols:
      if self.x_s in self.dr_xy.free_symbols: # optimize
        y_fun = lambdify(x,self.dr_xy.subs({self.x_s: x}).as_set().start)
        y_min = minimize(y_fun,[0.0]).fun
        y_fun = lambdify(x,-1*self.dr_xy.subs({self.x_s: x}).as_set().end)
        y_max = -minimize(y_fun,[0.0]).fun
      else: # just an interval in y
        y_min = self.dr_xy.as_set().start
        y_max = self.dr_xy.as_set().end
    else:
      y_min,y_max = -oo,oo
    if self.x_s in self.dr_xy.free_symbols:
      if self.y_s in self.dr_xy.free_symbols: # optimize
        x_fun = lambdify(y,self.dr_xy.subs({self.y_s: y}).as_set().start)
        x_min = minimize(x_fun,[0.0]).fun
        x_fun = lambdify(y,-1*self.dr_xy.subs({self.y_s: y}).as_set().end)
        x_max = -minimize(x_fun,[0.0]).fun
      else: # just an interval in x
        x_min = self.dr_xy.as_set().start
        x_max = self.dr_xy.as_set().end
    else:
      x_min,x_max = -oo,oo
    self.x_r = [x_min,x_max]
    self.y_r = [y_min,y_max]
  
  def rt_projector(self):
    # project dr_rt onto r and theta
    raise NotImplementedError('projection of design region in rt onto r and theta')
    var('r',real=True)
    var('t',real=True)
    if self.theta_s in self.dr_rt.free_symbols:
      if self.r_s in self.dr_rt.free_symbols: # optimize
        # TODO this is giving me trouble because it has a cos of the variable I want as an interval
        theta_fun1 = lambda r: self.dr_rt.subs({self.r_s: r})
        theta_fun2 = lambda r: theta_fun1(r).as_set().start
        # print(theta_fun1(1.2))
        theta_min = minimize(theta_fun2,[pi]).fun
        theta_fun = lambdify(r,-1*self.dr_rt.subs({self.r_s: r}).as_set().end)
        theta_max = -minimize(theta_fun,[0.0]).fun
      else: # just an interval in theta
        theta_min = self.dr_rt.as_set().start
        theta_max = self.dr_rt.as_set().end
    else:
      theta_min,theta_max = -oo,oo
    if self.r_s in self.dr_rt.free_symbols:
      if self.theta_s in self.dr_rt.free_symbols: # optimize
        r_fun = lambdify(theta,self.dr_rt.subs({self.theta_s: theta}).as_set().start)
        r_min = minimize(r_fun,[0.0]).fun
        r_fun = lambdify(theta,-1*self.dr_rt.subs({self.theta_s: theta}).as_set().end)
        r_max = -minimize(r_fun,[0.0]).fun
      else: # just an interval in x
        r_min = self.dr_rt.as_set().start
        r_max = self.dr_rt.as_set().end
    else:
      r_min,r_max = -oo,oo
    self.r_r = [r_min,r_max]
    self.theta_r = [theta_min,theta_max]

  # plot!
  def plot_dr(self):
    p = plot_implicit(
      self.dr_xy,
      x_var=self.x_s,
      y_var=self.y_s,
      xlabel='Re',
      ylabel='Im')
    p.show()

    
#############################################################

############## Transient Characteristic Input ###############

#############################################################

    """
    Waiting for Dr. Picone to add dr_xy, dr_zw, dr_rt functions.
    Need to figure out how my functions will interact with the dr
    """
    
    # do we update parameters in other dr in conversion functions?
    # could we have the user just update 1 value at a time?


    def OS_based(self, expr):
        #############################################
        ################ NOT WORKING ################
        #############################################
        # in dr_zw
        OS = self.OS_s
        z = self.z_s
        wn = self.wn_s

        # convert OS range into zw
        expr2 = expr.subs({OS: 100 * sp.exp(-z * sp.pi / (sp.sqrt(1 - z ** 2)))})

        # add expr2 to dr_zw
        # self.dr_zw(expr2) ???

        # Convert from zw to xy then update dr_xy
        OS_xy = self.zw_to_xy(expr2)
        self.dr_xy(OS_xy)

        # Convert from zw to rt then update dr_rt
        OS_rt = self.zw_to_rt(expr2)
        self.dr_rt(OS_rt)


    def Tp_based(self, expr):
        #############################################
        ################ NOT WORKING ################
        #############################################
        # in dr_zw
        Tp = self.Tp_s
        z = self.z_s
        wn =  self.wn_s

        # Tp = pi/wd, wd = wn*sp.sqrt(1 - z^2)
        expr2 = expr.subs({Tp: sp.pi/(wn*sp.sqrt(1 - z^2)) })

        self.dr_zw(expr2)

        Tp_xy = self.zw_to_xy(expr2)
        self.dr_xy(Tp_xy)

        Tp_rt = self.zw_to_rt(expr2)
        self.dr_rt(Tp_rt)


    def Ts_based(self, expr):
        #############################################
        ################ NOT WORKING ################
        #############################################
        # in dr_xy
        Ts = self.Ts_s
        x = self.x_s
        y = self.y_s

        expr2 = expr.subs({Ts: -4/x})

        self.dr_xy(expr2)

        Ts_zw = self.xy_to_zw(expr2)
        self.dr_zw(Ts_zw)

        Ts_rt = self.xy_to_rt(expr2)
        self.dr_rt(Ts_rt)


    def xy_based(self, expr):
        #############################################
        ################ NOT WORKING ################
        #############################################
        # in dr_xy

        x = self.x_s
        y = self.y_s

        self.dr_xy(expr)

        xy_zw = self.xy_to_zw(expr)
        self.dr_zw(xy_zw)

        xy_rt = self.xy_to_rt(expr)
        self.dr_rt(xy_rt)



    def zw_based(self, expr):
        #############################################
        ################ NOT WORKING ################
        #############################################
        # in dr_zw

        z = self.z_s
        wn = self.wn_s

        self.dr_zw(expr)

        zw_rt = self.zw_to_rt(expr)
        self.dr_rt(zw_rt)

        zw_xy = self.zw_to_xy(expr)
        self.dr_rt(zw_xy)
                  

    def rt_based(self, expr):
        #############################################
        ################ NOT WORKING ################
        #############################################
        # in dr_rt

        r = self.r_s
        theta = self.theta_s

        self.dr_rt(expr)

        rt_xy = self.rt_to_zw(expr)
        self.dr_xy(rt_xy)

        rt_zw = self.rt_to_zw(expr)
        self.dr_zw(rt_zw)
