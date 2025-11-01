# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:36:27 2025

@Written and Directed by: Sathwik
"""

import random
import sys
n=random.randint(0, 100)
for i in range(5):
    g=int(input("guess a number between 0 to 100:"))

    if g<n:
        print("too low, try again !")
    if g>n:
        print("too high, try again !")
    if g==n:
        print("correct guess!!!, you are very lucky today.")
        sys.exit()
print("too bad better luck next time, the number was:",n)
        
