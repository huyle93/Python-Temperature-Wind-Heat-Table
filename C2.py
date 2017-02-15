#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:54:39 2017

@author: HLe
"""

####### functions #######

def to_f(cel): # Convert fahrenheit to celsius
    return (cel * 9/5)+32
def wc(c,f):
    wc_list = []
    wc_list.append(c)
    wc_list.append(f)
    for val in range (5,41,5):
        if (f <= 50):
            windchill = 35.74 + (0.6215*f) - 35.75*(val**0.16) + 0.4275*f*(val**0.16)
            windchill = round(windchill, 2)
        else:
            windchill = "x"
        wc_list.append(windchill)
    return(wc_list)
def heat(c,f):
    heat_list = []
    heat_list.append(c)
    heat_list.append(f)
    for val in range (40,100,10):
        if (f >= 80):
            heatindex = -42.379 + 2.04901523*f + 10.14333127*val + -0.22475541*f*val + -6.83783*10**-3 *f**2 + -5.481717*10**-2 * val**2 + 1.22874*10**-3 * f**2 * val + 8.5282*10**-4 * f * val**2 + -1.99*10**-6 * f**2 * val**2
            heatindex = round(heatindex, 2)
        else:
            heatindex = "x"
        heat_list.append(heatindex)
    return(heat_list)
#########################

val1, val2 = input("Enter two numbers between -20 and 50: ").split()
intVal1 = int(val1)
intVal2 = int(val2)
if intVal1 < -20 or intVal2 > 50:
    print("Number Invalid")
else:
    #print("{0} {1}".format(intVal1, intVal2))
    print("Wind chill temperatures")
    print("{0}{1}{2:>8}".format("Celsisu","\t", "Fahr"),"\t", end=" ")
    for val in range (5, 45, 5):
        print(val,"\t", end = " ")
    print('\n')
    flist = []
    for val in range (intVal1, intVal2 + 1):
        f = to_f(val)
        list1 = []
        list1 = (wc(val,f))
        for i in list1:    
            print(i, end="\t")
        print()
    print('\n')
    ####################################################################
    print("Heat Index Temp")
    print("{0}{1}{2:>8}".format("Celsisu","\t", "Fahr"),"\t", end=" ")
    for val in range (40, 100, 10):
        print(val,"%","\t", end = " ")
    print('\n')
    flist = []
    for val in range (intVal1, intVal2 + 1):
        f = to_f(val)
        list1 = []
        list1 = (heat(val,f))
        for i in list1:    
            print(i, end="\t")
        print()