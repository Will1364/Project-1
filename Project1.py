#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:47:58 2022

@author: annaemilielundeborre
"""

import numpy as np
import pandas as pd


while True:
    try:
        fileName = str(input("Which datafile should be analysed?:"))
        open(fileName)
        break
    except IOError:
        print("Not a valid filename. have you remembered to write. ")



        
        
def dataLoad(filename):
        # Loade filen
    file = open(filename).read()
        #String split
    s=file.split()
    s = np.asfarray(s,float)
        #len af filen, dividere med tre, for antallet af rækker
    l = int(len(s)/3)
        #Foerste række
    k=np.array([s[0],s[1],s[2]])
    
   # s=s.astype(np.float)


        #Loop for at stacke matricen
    for i in range (1,l):
        #BacName datafejls håndtering
        if s[i*3+2] >= 1 and s[i*3+2] <= 4:
          if s[i*3] >= 10 and s[i*3] <= 60:
              if s[i*3+1] > 0:
                  v = np.array([s[i*3],s[i*3+1],s[i*3+2]])
                  k = np.vstack ((k,v))

    
    data = k

    
    return data

print(dataLoad("test.txt"))




    
