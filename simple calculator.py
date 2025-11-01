# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:36:27 2025

@Written and Directed by: Sathwik
"""

import sys
print("    ***************")
print("    *   welcome   *")
print("    *      to     *")
print("    *  calculator *")
print("    ***************")
print(" ")
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
print(" ")
print("enter you choice:")
print("1- for addition")
print("2- for subtraction")
print("3- for multiplication")
print("4- for division")
print(" ")
c=int(input("enter your choice now:"))
print(" ")
if c == 1:
    s=x+y
elif c==2:
    s=x-y
elif c==3:
    s=x*y
elif c==4:
    s=x/y
else:
    print("invalid choice!!!!!")
    sys.exit()

   
print("solution=",s)
print("*****************")