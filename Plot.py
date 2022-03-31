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
