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
           
####################################################################################################################################################################
#Denne del indlæser datafil og omdanner  til matrice

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
                else:
                    print("Datafejl i kolonne 2, række " + str(i+1))
            else:
                print("Datafejl i kolonne 1, række " + str(i+1))
        else:
            print("Datafejl i kolonne 3, række " + str(i+1))
    print("Rækker med datafejl er frasorteret")
    time.sleep(2)
    data = k
    dataBackup = data   #en backup af den indlæste data gemmes i programmet, så man altid kan vende tilbage selv efter man har filtreret data
    
    return data

##################################################################################################################################################################
#Denne del returnerer Statistik

def dataStatistics(data, statistic):
        #hvad dette stykke kode skal udregne bliver bestemt via en række if-sætninger
    if statistic == "Mean Temperature":
        result = np.mean(data[:,0])    #mean temperature bliver beregnet ved at finde gennemsnittet af elementerne i øverste række
    elif statistic == "Mean Growth rate":
        result = np.mean(data[:,1])    #mean growth rate bliver beregnet ved at finde gennemsnittet af elementerne i midterste række
    elif statistic == "Rows":
        result = np.size(data[:,0])    #antallet af rows i data bliver beregnet som længden af den øverste række
    elif statistic == "Std Temperature":
        result = np.std(data[:,0])     #std temperature er std deviation af temperaturmålingerne og det bliver udregnet via np.std af den øverste række af dataT
    elif statistic == "Std Growth rate":
        result = np.std(data[:,1])     #std growth rate er std deviation af temperaturmålingerne og det bliver udregnet via np.std af den øverste række af dataT
    elif statistic == "Mean Cold Growth rate":
        v = data[:,1][data[:,0] < 20] #der bliver skabt en vektor med alle de værdier for growth rate som har samme plads som       
        result = np.mean(v)
    elif statistic == "Mean Hot Growth rate":
        v = data[:,1][data[:,0] > 20]                
        result = np.mean(v)    
    return result
  
 ##################################################################################################################################################################
#denne del filtrerer data

def dataFilter(filtertype, betingelse):
    if filtertype == bacteria:
        l = np.size(data[:,0]) #l er antallet af rækker i datamatricen
        V = np.zeros(3) #der bliver oprettet en vector med 3 0'er
        for i in range(l):
            if data[i,2] == betingelse:
                V = np.vstack ((V,data[i,:])) # de rækker i datamatricen som opfylder betingelsen bliver tilføjet til V
        
        V = np.delete(V,0,0) #den første linje i matrixcen V som blot er 0'er bliver slettet igen, så matricen udelukkende indeholder data
        data = V
    elif filtertype == growthrate:
        for i in range(l):
            if data[i,1] >= betingelse[0] and data[i,1] <= betingelse[1]: #her er betingelsen i form af en vektor bestående af øvre og nedre grænse i intervallet
                V = np.vstack ((V,data[i,:]))
        V = np.delete(V,0,0)
        data = V
        

####################################################################################################################################################################
#denne del laver plots

def dataPlot(data):
    
    Saen=data[data[:,2]==1]
    Saen=data[data[:,2]==1]
    Bace=data[data[:,2]==2]
    Li=data[data[:,2]==3]
    Brth=data[data[:,2]==4]
    
    
    langs=['Salmonella','Bacillus','Listeria','Brochothrix']
  
    number=[np.sum(Saen[:,1]),np.sum(Bace[:,1]),np.sum(Li[:,1]),np.sum(Brth[:,1])]
    
    plt.bar(langs,number,align='center',alpha=0.5)
    #plt.xticks(langs, y)
    plt.ylabel('Amount')
    plt.title('Number og bacteria')
    plt.show()

#plot 2
 #Næste plot af de fire grafer for growth rate iforhold til temp
    
def dataPlot2(data):
            temp = np.array(data[:,0]) #Finder temperturen i dataen
            growth = np.array(data[:,1]) #Finder growth rate dataen
            
            temp1 = np.ones(np.size(temp),dtype=bool)# Laver en vektor med størrelse 1
            growth1 = np.ones(np.size(growth),dtype=bool)# Laver en vektor med størrelse 1
            
        #Det samme gentages for de andre temperaturer, samt bakterier
            
            temp2 = np.ones(np.size(temp),dtype=bool) 
            growth2 = np.ones(np.size(growth),dtype=bool) 
            temp3 = np.ones(np.size(temp),dtype=bool) 
            growth3 = np.ones(np.size(growth),dtype=bool)
            temp4 = np.ones(np.size(temp),dtype=bool) 
            growth4 = np.ones(np.size(growth),dtype=bool) 


            for i in range(len(temp)):
                if not (data[i,2] == 1):
                    temp1[i] = False #Dem der ikke er lig 1 er false
                    growth1[i] = False #Dem der ikke er lig 1 er false
            temp1x = np.array(temp[temp1]) #x-værdi for bakterie 1
            growth1y = np.array(growth[growth1]) #y-værdi for bakterie 1

            for i in range(len(temp)): #Loopet gentages
                if not (data[i,2] == 2):
                    temp2[i] = False
                    growth2[i] = False
            temp2x = np.array(temp[temp2]) #x-væriden for bakterie 2
            growth2y = np.array(growth[growth2]) #y-værdien for bakterie 2

            for i in range(len(temp)): #Loopet gentages
                if not (data[i,2] == 3):
                    temp3[i] = False
                    growth3[i] = False
            temp3x = np.array(temp[temp3])  # x-væriden for bakterie 3
            growth3y = np.array(growth[growth3]) # y-værdien for bakterie 3
            
            for i in range(len(temp)): #Loopet gentages
                if not (data[i,2] == 4):
                    temp4[i] = False
                    growth4[i] = False
            temp4x = np.array(temp[temp4])  # x-væriden for bakterie 4
            growth4y = np.array(growth[growth4]) # y-værdien for bakterie 4

    # Sorterer de forskellige rækker data
            sortorder1 = np.argsort(temp1x)
            temp1x = temp1x[sortorder1] 
            growth1y = growth1y[sortorder1] 
            sortorder2 = np.argsort(temp2x) 
            temp2x = temp2x[sortorder2] 
            growth2y = growth2y[sortorder2] 
            sortorder3 = np.argsort(temp3x)
            temp3x = temp3x[sortorder3] 
            growth3y = growth3y[sortorder3] 
            sortorder4 = np.argsort(temp4x) 
            temp4x = temp4x[sortorder4] 
            growth4y = growth4y[sortorder4] 
  
    #Plotter plottet
    #Plottet punkterne på grafen
            plt.scatter(temp1x, growth1y,color="purple")
            plt.scatter(temp2x, growth2y,color="cyan")
            plt.scatter(temp3x, growth3y,color="blue")
            plt.scatter(temp4x, growth4y,color="magenta")
            plt.title('Growth rate by temperature') #Titel
            plt.xlabel('Temperature') #Navn x-aksen
            plt.ylabel('Growth rate') #Navn y-aksen
            plt.xlim([10, 60]) #Sætter interval på x-aksen
            plt.ylim([0,1]) #Sætter interval på y-aksen
            plt.plot(temp1x, growth1y, label = 'Salmonella', color="purple") 
            plt.plot(temp2x, growth2y, label = 'Bacillus', color="cyan") 
            plt.plot(temp3x, growth3y, label = 'Listeria', color="blue") 
            plt.plot(temp4x, growth4y, label = 'Brochothrix', color="magenta") 
            plt.legend(loc="upper right")
            plt.show() 
        
        
        

####################################################################################################################################################################
#Her er den aktive del af koden
#################################################################################################################################################################

#####################################################################################################################################################################
#Denne del viser menuen

while status == 1: #programmet vil altid vende tilbage til hovedmenuen, ved mindre status ændres til 0
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
                if dataRead == 0: #hvis brugeren prøver at behandle data før programmet har indlæst noget data, vil er blive kaldt missingData fejl
                    raise missingData
            break
        except missingData: #hvis der mangler data foreslår programmet at indlæse data
            print("""Data mangler! Denne funktion er ikke mulig uden data.
            Indlæs venligst data""")
            
        except wrongString:        #hvis der er intastet forkert string, vil programmet foreslå at tjekke for stavefejl
            print("Dette input er ikke gyldigt. Tjek evt. for stavefejl og prøv igen.")
            
        except ValueError:        #hvis der er intastet noget andet end en string, vil programmet minde brugeren om at input skal være en string
            print("Dette input er ikke gyldigt. Input skal være tekst")
   
    #######################################################################################################################################################################
    #Dette er brugergrænsefladen for indlæs data

    if Command == "Indlæs data":        
        while True:
            try:
                filename = str(input("Hvilken datafil skal indlæses?:"))        #User bliver bedt om et filnavn som input
                open(filename)                                                      #programmet prøver at åbne filen med angivet filnavn
                break
            except IOError:                                                         #I tilfælde af at det ikke er lykkedes at åbne en fil filename, bedes brugeren om at prøve igen
                  print("Der er ikke fundet en fil med dette filnavn")
                  print("Har du husket at slutte filnavnet med .txt?")
                  print("Prøv igen.")
                  time.sleep(3)
        print("Filen er lokaliseret")
        time.sleep(1)
        print("Datafilen indlæses")
        time.sleep(1)
        data = dataLoad(filename)
        dataRead = 1 #programmet husker at den nu har loaded data
        print("Filen er nu indlæst")
        time.sleep(3)
        print("""
            
            
              """)   

        
    #######################################################################################################################################################################
    #Dette er brugergrænsefladen for indlæs data
        
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
        while True:
            
            try:
                statistic = str(input("Indtast venligst dit valg:"))      #programmet beder brugeren vælge en statistik
                if statistic != "Mean Temperature" and statistic != "Mean Growth rate" and statistic != "Rows" and statistic != "Std Temperature" and statistic != "Std Growth rate" and statistic != "Mean Cold Growth rate" and statistic != "Mean Hot Growth rate" and statistic != "Tilbage":
                    raise wrongString    #hvis brugeren intaster en forkert string vil der blive kaldt en NameError                                                           
                break
            except wrongString:
                print("Dette input er ikke gyldigt. Tjek evt. for stavefejl og prøv igen.")
            except ValueError:
                print("Dette input er ikke gyldigt. Input skal være tekst")
        if statistic != "Tilbage":
            print(dataStatistics(data, statistic))
            time.sleep(3)
        print("""
            
            
              """)    
    
    
    if Command == "Generer diagrammer":
        print("""Du kan nu vælge følgende grafer:     #undermenu viser brugeren hvilke former for statistik programmet kan fremstille
        - Number of bacteria
        - Growth rate by temperature
        
        - Tilbage""")
        while True:
            
            try:
                plotType = str(input("Indtast venligst dit valg:"))      #programmet beder brugeren vælge en statistik
                if plotType != "Number of bacteria" and plotType != "Growth rate by temperature" and plotType != "Tilbage":
                    raise wrongString    #hvis brugeren intaster en forkert string vil der blive kaldt en NameError                                                           
                break
            except wrongString:
                print("Dette input er ikke gyldigt. Tjek evt. for stavefejl og prøv igen.")
            except ValueError:
                print("Dette input er ikke gyldigt. Input skal være tekst")
        if  plotType == "Number of bacteria"
            print(dataPlot(data))
        elif plotType == "Growth rate by temperature"
            print(dataPlot2(data))
            time.sleep(3)
        print("""
            
            
              """)    
    
    
    
        
    ####################################################################################################################################################################
    #Programmet afsluttes
    ######################################################################################################################################################################
    
    if Command == "Afslut":
        status = 0
      
    
            
