# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:50:43 2021

@author: Saadia Bayou
"""


import matplotlib.pyplot as plt
import numpy as np

c=3*10e+8

dl1=0.43 # A
l0=6300


#l02=6300

#lobs=
#l=
#l03=6302
dlB1=0.58 # A
dlB2=0.54
dlB3=0.50

dl1=0.58
dl2=0.54
dl3=0.50


l01=0.44
l02=0.42
l03=0.45

def vit_rad(dl,l0):
    return c*(dl/l0)

#def vit_rad_2(l,l0):
#    return c*((lobs-l)/l0)


def vit_rot(dl,l0):
    return c*(dl/l0)



#vr1=vit_rad_1(dl,l0)
vr1=vit_rad(dl1,l01)
print("\nvrad_Fe1=",round(vr1,3), "km/s")


vr2=vit_rad(dl2,l02)
print("\nvrad_Fe2=",round(vr2,3))

vr3=vit_rad(dl3,l03)
print("\nvrad_Fe1=",round(vr3,3), "km/s")





print("\nBeltegueuse")



vrB1=vit_rot(dlB1,l0)
print("\nvrot_Fe1=",round(vrB1,3))

#dlB2=0.43 # A
#l02=6301

vrB2=vit_rot(dlB2,l0)
print("\nvrot_Fe2=",round(vrB2,3))

#dlB3=0.43 # A
#l03=6301

vrB3=vit_rot(dlB3,l0)
print("\nvrot_Fe3=",round(vrB3,3))



