# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:01:43 2022

@author: fmuror02
"""

txt = ("0000000000"*10000000)

print('Creating document...')
print('Aproximate timing of 1 minute.')

f = open("LD+","w")
f.write(txt)
f.close()

print()
print("'Large document +' creation is complete.")

#While True:
    #{code} is possible too.