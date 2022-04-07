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
        fileName = str(input("Which datafile should be analysed?:"))        #User bliver bedt om et filnavn som input
        open(fileName)                                                      #programmet prøver at åbne filen med angivet filnavn
        break
    except IOError:                                                         #I tilfælde af at det ikke er lykkedes at åbne en fil filename, bedes brugeren om at prøve igen
        print("Not a valid filename.")
        print("Have you remembered to end filename with .txt?")
        print("Please try again.")


        
        
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


def dataStatistics(data, statistic):
    
    dataT =data.t #matricen bliver transponeret til en 3xN matrice så temperaturen vil være i øverste række, growth rate vil være i midten og bacterietypen vil være i nederste række.

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
        v = dataT[1,:][dataT[0,:] < 20] #der bliver skabt en vektor med alle de værdier for growth rate som har samme plads som       
        result = np.mean(v)
    elif statistic == "Mean Hot Growth rate"
        v = dataT[1,:][dataT[0,:] > 20]                
        result = np.mean(v)

        
    return result

    
