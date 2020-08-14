Design region class 
-------------------------------------------

This documents the `design_region` class from the control package. The main objective of this class is to aid in the design of a controller.


Introduction
============

The 'design_region' module is intended to help document and define the design limits of a complex-plane dominant-pole system. All converted values are extrapolated using second-order approximations.


Variables and Parameters
========================

The permissible design region parameters are:

* x, y: 
    - X corresponds to the real axis of the complex plane.
    - y corresponds to the imaginary axis of the complex plane.
* r, theta:
    - r is the magnitude of a vector on the complex plane
    - theta is the anticlockwise angle from the positive real axis to the vector, in radians
* z, wn:
    - z is short for zeta, the damping ratio in this context
    - wn is short for omega subscript n, the natural frequency
* OS, Ts, Tr, Tp are in development:
    - OS is the overshoot ratio, not percent overshoot
    - Ts is the settling time
    - Tr is the rise time
    - Tp is the peak time

Use
===
Example code can be found at  
https://github.com/ricopicone/python-control/blob/design_region/examples/design_region_example_01.py

General use of the design region will follow the procedure below:

1. Create design region instance

2. Define parameter limitations
    
    While single values are allowed, the purpose of the design region is to provide ranges for all design parameters, such as [15,20].

3. Convert region parameters as desired

4. Plot design region

Public Methods and Functions
============================

**Design Region Mapping Methods:**

*Purpose:*

These methods take symbolic expressions from one coordinate paradigm and pass those expressions to another paradigm. 

*Use:*

The action of passing one set of symbolic expressions from one paradigm to the other is done when the method is called, no arguments are to be passed. 

*List of Methods:*
    - zw_to_rt: Maps damping ratio and natural frequency coordinates to magnitude and theta
    - rt_to_zw: Maps magnitude and theta coordinates to damping ratio and natural frequency
    - rt_to_xy: Maps magnitude and theta coordinates to complex plane coordinates, x being real and y being imaginary
    - xy_to_rt: Maps complex plane coordinates to magnitude and theta
    - zw_to_xy: Maps damping ratio and natural frequency coordinates to complex plane coordinates
    - xy_to_zw: Maps complex plane coordinates to damping ratio and natural frequency

*example:*

dr1.r = [1,4]

dr1.t = [3*pi/4,7*pi/8]

dr1.xy = dr1.rt_to_xy()

print(dr1.xy)

>"(1 <= sqrt(x_s**2 + y_s**2)) & (sqrt(x_s**2 + y_s**2) <= 4) & (atan(y_s/x_s) - pi <= pi) & (atan(y_s/x_s) - pi >= pi/2)"

**Coordinate Tranformations:**

*Purpose:*

These functions convert values (symbolic and float have both been confirmed to work) from one coordinate paradigm to another, using the second order approximation where appropriate.

*Use:*

Most functions require two arguments with the exception of 'co_Ts_to_x' and 'co_OS_to_z' which simply require one. The functions then return transformed values corresponding to the coordinate paradigm.

*List of Functions:*
    
    - co_xy_to_rt: Converts complex plane coordinates to magnitude and theta
    - co_rt_to_xy: Converts magnitude and theta coordinates to complex plane coordinates, x being real and y being imaginary
    - co_zw_to_rt: Converts damping ratio and natural frequency coordinates to magnitude and theta
    - co_rt_to_zw: Converts magnitude and theta coordinates to damping ratio and natural frequency
    - co_xy_to_zw: Maps complex plane coordinates to damping ratio and natural frequency
    - co_zw_to_xy: Maps damping ratio and natural frequency coordinates to complex plane coordinates
    - co_OS_to_z: Converts an overshoot ratio (not percent) requirement to the corresponding damping ratio
    - co_Ts_to_x: Converts a settling time requirement to the corresponding real axis value (for differential compensators)
    - co_TsOS_to_xy: Converts overshoot ratio and settling time requirements to corresponding real and imaginary axis values (for differential compensators)

*example:*

print((dr1.co_OS_to_z(0.10)).evalf)

>"0.591155033798897"


**Interval Maps**

*Documentation Pending*

Design Region Projections 

*Documentation Pending*

Plotting 

*Documentation Pending*

Private Methods and Functions
=============================

