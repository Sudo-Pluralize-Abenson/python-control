Design region class (from the design_region module)
-------------------------------------------

This documents the `design_region` class from the `design_region.py` module.


Introduction
============

The 'design_region' module is intended to help document and define the design
limits of a complex-plane dominant-pole system. All converted values are extrapolated
using second-order approximations.


Variables and Parameters
========================

The permissible design region parameters are:
- x, y: 
    - X corresponds to the real axis of the complex plane
    - y corresponds to the imaginary axis of the complex plane, only positive values considered
- r, theta:
    - r is the magnitude of a vector on the complex plane
    - theta is the anticlockwise angle from the positive real axis to the vector, in radians
- z, wn:
    - z is short for zeta, the damping ratio in this context
    - wn is short for omega subscript n, the natural frequency
-OS, Ts, Tr, Tp are in development:
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
     - While single values are allowed, the purpose of the design region 
       is to provide ranges for all design parameters, such as [15,20].
3. Convert region parameters as desired
4. Plot design region


