#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:47:58 2022

@author: annaemilielundeborre
"""

import numpy as np
import pandas as pd

def dataLoad(filename):
        # Loade filen
    file = open(filename).read()
        #String split
    s=file.split()
        #len af filen, dividere med tre, for antallet af rækker
    l = int(len(s)/3)
        #Foerste række
    k=np.array([s[0],s[1],s[2]])
    
        #Loop for at stacke matricen
    for i in range (1,l):
        
        v = np.array([s[i*3],s[i*3+1],s[i*3+2]])
        
        k = np.vstack ((k,v))
    
    data = k

    
    return data

print(dataLoad("test.txt"))




    