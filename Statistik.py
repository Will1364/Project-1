# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:09:03 2022

@author: willi
"""

with with numpy as np

def dataStatistics(data, statistic):
    
    dataT =data.t   #matricen bliver transponeret til en 3xN matrice så temperaturen vil være i øverste række, growth rate vil være i midten og bacterietypen vil være i nederste række.
    
    #hvad dette stykke kode skal udregne bliver bestemt via en række if-sætninger
    if statistic == "Mean Temperature"
        result = np.mean(dataT[0,:])    #mean temperature bliver beregnet ved at finde gennemsnittet af elementerne i øverste række
    elif statistic == "Mean Growth rate"
        result = np.mean(dataT[1,:])    #mean growth rate bliver beregnet ved at finde gennemsnittet af elementerne i midterste række
    elif statistic == "Rows"
        result = np.size(dataT[0,:])    #antallet af rows i data bliver beregnet som længden af den øverste række
    elif statistic == "Std Temperature"
        result = np.std(dataT[0,:])     #std temperature er std deviation af temperaturmålingerne og det bliver udregnet via np.std af den øverste række af dataT
    elif statistic == "Std Growth rate"
        result = np.std(dataT[1,:])     #std growth rate er std deviation af temperaturmålingerne og det bliver udregnet via np.std af den øverste række af dataT
    elif statistic == "Mean Cold Growth rate"
        result =
        
        
    return result
