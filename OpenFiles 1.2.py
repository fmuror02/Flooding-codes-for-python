# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:59:23 2022

"""

n = 0
txt = ('0000000000'*10000)
while True:
    f = open(f'f{n}.txt','w')
    f.write(txt)
    f.close()
    
    print(n)
    n = n + 1
    del f




    

