import numpy as np
import matplotlib.pyplot as plt

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

print(dataPlot(dataLoad('test.txt')))
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

print(dataPlot2(dataLoad('test.txt')))
