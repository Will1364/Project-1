#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:47:58 2022

@author: annaemilielundeborre & William Hedegaard Langvad s214512
"""


#####################################################################################################################################################################
#Setup
#####################################################################################################################################################################
import time
import numpy as np
import pandas as pd

dataRead = 0  #denne variabel holder styr på om programmet har noget data at arbejde med
class missingData(Exception): #Error type defineret for tilfælde hvor brugeren vil behandle data før han/hun har givet det til programmet
    pass
class wrongString(Exception): #Error type defineret for tilfælde hvor brugeren skriver et input forkert
    pass
status = 1


#####################################################################################################################################################################
#Denne del viser menuen
#####################################################################################################################################################################
while status == 1 #programmet vil altid vende tilbage til hovedmenuen, ved mindre status ændres til 0
    print(""""Velkommen til hovedmenuen, dette program kan behandle dit data for dig. #hovedmenu tekst
      Du har nu følgende valgmuligheder:
      - Indlæs data
      - Filtrer data
      - Vis statistik
      - Generer diagrammer
      - Afslut""")



    while True:
        try:
            Command = str(input("Indtast vænligst dit valg:")) #programmet spørger hvilken funktion brugeren ønsker at bruge
            
            if Command != "Indlæs data" and Command != "Filtrer data" and Command != "Vis statistik" and Command != "Generer diagrammer" and Command != "Afslut": 
                raise wrongString #hvis brugeren intaster en forkert string vil der blive kaldt en NameError
            
            if Command == "Filtrer data" or Command == "Vis statistik" or Command == "Generer diagrammer":
                if DataRead == 0: #hvis brugeren prøver at behandle data før programmet har indlæst noget data, vil er blive kaldt missingData fejl
                    raise missingData
            break
        except missingData: #hvis der mangler data foreslår programmet at indlæse data
            print("""Data mangler! Denne funktion er ikke mulig uden data.
            Indlæs venligst data""")
            
        except wrongString:        #hvis der er intastet forkert string, vil programmet foreslå at tjekke for stavefejl
            print("Dette input er ikke gyldigt. Tjek evt. for stavefejl og prøv igen.")
            
        except ValueError:        #hvis der er intastet noget andet end en string, vil programmet minde brugeren om at input skal være en string
            print("Dette input er ikke gyldigt. Input skal være tekst")

        
        
    ####################################################################################################################################################################
    #Denne del indlæser datafil og omdanner  til matrice
    ####################################################################################################################################################################
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

    if Command == "Indlæs data":        
        while True:
            try:
                fileName = str(input("Which datafile should be analysed?:"))        #User bliver bedt om et filnavn som input
                open(fileName)                                                      #programmet prøver at åbne filen med angivet filnavn
                break
            except IOError:                                                         #I tilfælde af at det ikke er lykkedes at åbne en fil filename, bedes brugeren om at prøve igen
                  print("Not a valid filename.")
                  print("Have you remembered to end filename with .txt?")
                  print("Please try again.")
        data = dataLoad(filename)
      
        dataRead = 1 #programmet husker at den nu har loaded data



    ##################################################################################################################################################################
    #Denne del returnerer Statistik
    ##################################################################################################################################################################



    def dataStatistics(data, statistic):
    
        dataT =data.t #matricen bliver transponeret til en 3xN matrice så temperaturen vil være i øverste række, growth rate vil være i midten og bacterietypen vil være i nederste række.

        #hvad dette stykke kode skal udregne bliver bestemt via en række if-sætninger
        if statistic == "Mean Temperature":
            result = np.mean(dataT[:,0])    #mean temperature bliver beregnet ved at finde gennemsnittet af elementerne i øverste række
        elif statistic == "Mean Growth rate":
            result = np.mean(dataT[:,1])    #mean growth rate bliver beregnet ved at finde gennemsnittet af elementerne i midterste række
        elif statistic == "Rows":
            result = np.size(dataT[:,0])    #antallet af rows i data bliver beregnet som længden af den øverste række
        elif statistic == "Std Temperature":
            result = np.std(dataT[:,0])     #std temperature er std deviation af temperaturmålingerne og det bliver udregnet via np.std af den øverste række af dataT
        elif statistic == "Std Growth rate":
            result = np.std(dataT[:,1])     #std growth rate er std deviation af temperaturmålingerne og det bliver udregnet via np.std af den øverste række af dataT
        elif statistic == "Mean Cold Growth rate":
            v = dataT[:,1][dataT[:,0] < 20] #der bliver skabt en vektor med alle de værdier for growth rate som har samme plads som       
            result = np.mean(v)
        elif statistic == "Mean Hot Growth rate":
            v = dataT[:,1][dataT[:,0] > 20]                
            result = np.mean(v)    
        return result

    if Command == "Vis statistik":
        print("""Du har nu følgende valgmuligheder:     #undermenu viser brugeren hvilke former for statistik programmet kan fremstille
        - Mean Temperature
        - Mean Growth rate
        - Rows
        - Std Temperature
        - Std Growth rate
        - Mean Cold Growth rate
        - Mean Hot Growth rate
        - Afslut""")
        try:
            statistic = str(input("Indtast venligst dit valg:"))      #programmet beder brugeren vælge en statistik
            if Command != "Mean Temperature" and Command != "Mean Growth rate" and Command != "Rows" and Command != "Std Temperature" and Command != "Std Growth rate" and Command != "Mean Cold Growth rate" and Command != "Mean Hot Growth rate" and Command != "Afslut":
                  raise wrongString    #hvis brugeren intaster en forkert string vil der blive kaldt en NameError                                                           
            break
        except wrongString:
            print("Dette input er ikke gyldigt. Tjek evt. for stavefejl og prøv igen.")
        except ValueError:
            print("Dette input er ikke gyldigt. Input skal være tekst")
      
      print(dataStatistics(data, statistic))
      time.sleep(3)
        print("""
              
              
              """)
      ####################################################################################################################################################################
      #Programmet afsluttes
      ######################################################################################################################################################################
      
      if Command == "Afslut":
            status = 0
      
      
            
