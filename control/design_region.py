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
Arif Islam
Alexander Benson
Aiden Hunter
Megan Taylor
Parth Gogate
Marcelino Figueroa

Date (initial): 2 October 2019
"""

# external modules
import numpy as np
#from sympy import core
import inspect
from scipy.optimize import minimize
import warnings
import sys
from sympy import * # update 8/6 : Arif. Fixes error with infinity sign and "Symbol not defiend error"

# variables to expose for import
__all__ = ['design_region'] 

# class definition!
class design_region():
    '''
    A class to define the design region and print the output.
    
    '''
    # attribute getters and setters
    @property
    def x(self):
        the_p = inspect.currentframe().f_code.co_name
        attribute = getattr(self,'_'+the_p)
        return self.attribute_getter(attribute)
    @x.setter
    def x(self,value):
        self.flagxy=True
        # check for valid values
        value = self.normalize_input(value)
        if value[1] > 0:
            raise Exception('x must be negative for stability')
        the_p = inspect.currentframe().f_code.co_name
        # this sets self.x=value
        exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
        
        
        if not self.is_calling_method_init(): # if not init call
            # x to dr_xy
            self.dr_xy = self.dr_xy & self.x_r
            # if not self.is_calling_method_setter(): #call not from setter
            #     # avoids loops
            #     # dr_xy to other drs
            #     self.xy_to_rt()
            #     self.xy_to_zw()
            #     # interval maps
            #     self.in_xy_to_rt(is_x=True)
            #     # TODO ...
        else: # if it is first call
            self.dr_xy = self.x_r
    #
    @property
    def y(self):
        the_p = inspect.currentframe().f_code.co_name
        attribute = getattr(self,'_'+the_p)
        return self.attribute_getter(attribute)
    @y.setter
    def y(self,value):
        self.flagxy=True
        # check for valid values
        value = self.normalize_input(value)
        #if value[0] < 0:
        #    raise Exception('y must be nonnegative')
        the_p = inspect.currentframe().f_code.co_name
        exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
        
        if not self.is_calling_method_init():
            # y to dr_xy
            self.dr_xy = self.dr_xy & self.y_r
            # if not self.is_calling_method_setter():
            #     # avoids loops
            #     # dr_xy to other drs
            #     self.xy_to_rt()
            #     self.xy_to_zw()
            #     # interval maps
            #     self.in_xy_to_rt(is_x=False)
            #     # TODO
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
        self.flagrt=True
        # check for valid values
        value = self.normalize_input(value)
        if value[0] < 0:
            raise Exception('r must be nonnegative [magnitude cannot be negative]')
        the_p = inspect.currentframe().f_code.co_name
        exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
        
        if not self.is_calling_method_init():
            # r to dr_rt
            self.dr_rt = self.dr_rt & self.r_r
            #if not self.is_calling_method_setter():
                # print('... r to other stuff')
                # # avoids loops
                # # dr_rt to other drs
                # self.rt_to_xy()
                # self.rt_to_zw()
                # # interval maps
                # self.in_rt_to_xy()
                # TODO
        else:
            self.dr_rt = self.r_r
    #
    @property
    def theta(self):
        the_p = inspect.currentframe().f_code.co_name
        attribute = getattr(self,'_'+the_p)
        return self.attribute_getter(attribute)
    @theta.setter
    def theta(self,value):
        self.flagrt=True
        # check for valid values
        value = self.normalize_input(value)
        value_in = Interval(*value)
        #print(value_in)
        #value_valid = Interval(pi/2,pi)
        #if not (value_in-value_valid).is_empty:
        #    raise Exception('theta must be between pi/2 and pi')
        the_p = inspect.currentframe().f_code.co_name
        exec("self._%s = %s" % (the_p,self.attribute_setter(value,the_p)))
        
        if not self.is_calling_method_init():
            # r to dr_rt
            self.dr_rt = self.dr_rt & self.theta_r
            #if not self.is_calling_method_setter():
                # avoids loops
                # dr_rt to other drs
                #self.rt_to_xy()
                #self.rt_to_zw()
                # interval maps
                #self.in_rt_to_xy()
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
        # pack into array if needed
        value = self.normalize_input(value)
        # update corresponding variable inequality
        if not hasattr(self,f"{attribute}_r"):
            exec(f"self.{attribute}_r = (self.{attribute}_s >= {value[0]}) & (self.{attribute}_s <= {value[1]})")
        else:
            exec(f"interval = self.{attribute}_r & (self.{attribute}_s >= {value[0]}) & (self.{attribute}_s <= {value[1]})")
            exec(f"interval = interval.as_set().as_relational(self.{attribute}_s)")
            exec(f"self.{attribute}_r = interval")
        return value

    def normalize_input(self,value):
        if not isinstance(value,list):
            value = [value,value] # make array
        value.sort() # works with oo
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
        #     each variable. These are really _projections_
        #     because they can depend on other variables.
        # variables
        self.x_s = Symbol('x_s',real=True)
        self.x = [-oo,0]
        self.y_s = Symbol('y_s',real=True)
        self.y = [-oo,oo]
        self.r_s = Symbol('r_s',real=True)
        self.r = [0,oo]
        self.theta_s = Symbol('theta_s',real=True)
        self.theta = [-oo,oo]
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
        #         dr_xy: x,y
        #         dr_rt: r,theta
        #         dr_zw: z,wn
        self.dr_xy = (self.x_r)&(self.y_r)
        self.dr_rt = (self.r_r)&(self.theta_r)
        self.dr_zw = (self.z_r)&(self.wn_r)
        self.flagrt=False
        self.flagxy=False

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
             theta: atan(y/x)-pi}
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
             theta: atan(y/x)-pi}
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
             theta: atan(y/x)-pi}
        ).subs(
            {r: wn,
             theta: pi - acos(z)}
        )
        return self.dr_zw

    ## general coordinate transformations

    def co_xy_to_rt(self,x,y):
        r = sqrt(x**2+y**2)
        if x == 0:
            t = pi/2
        else:
            t = atan(y/x)-pi
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

    ## Parameter to Coordinate Transformations
    def co_OS_to_z(self, OS):
        z = -ln(OS)/sqrt(pi**2 + ln(OS)**2)
        return z

    def co_Ts_to_x(self, Ts):
        x = -4/Ts
        return x

    def co_TsOS_to_xy(self, Ts, OS):
        x = self.co_Ts_to_x(Ts)
        y = -x*pi/ln(OS)
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
        self.flagrt=False

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
        self.flagxy=False

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
        if self.flagrt==True:
            p = plot_implicit(
                self.dr_rt,
                x_var=self.r_s,
                y_var=self.theta_s,
                xlabel='R',
                ylabel='Theta')
        elif self.flagxy==True:
            p = plot_implicit(
                self.dr_xy,
                x_var=self.x_s,
                y_var=self.y_s,
                xlabel='Re',
                ylabel='Im')
        self.flagxy=False
        self.flagrt=False
        p.show()

