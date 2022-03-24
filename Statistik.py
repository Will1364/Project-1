# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:09:03 2022

@author: willi
"""

with with numpy as np

def dataStatistics(data, statistic):
    
    dataT =data.t
    
    if statistic == "Mean Temperature"
        result = np.mean(dataT[0,:])
    elif statistic == "Mean Growth rate"
        result = np.mean(dataT[1,:])
    elif statistic == "Rows"
        result = np.size(dataT[0,:])
    elif statistic == "Std Temperature"
        result = np.std(dataT[0,:])
    elif statistic == "Std Growth rate"
        result = np.std(dataT[1,:])
    elif statistic == "Mean Cold Growth rate"
        result ==
        
        
    return result
