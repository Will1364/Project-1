# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:16:01 2022

@author: willi
"""

print(""""Velkommen, dette program kan behandle dit data for dig. 
      Du har nu følgende valgmuligheder:
      - Indlæs data
      - Filtrer data
      - Vis statistik
      - Generer diagrammer
      - Afslut""")



while True:
    try:
        Command = str(input("Indtast vænligst dit valg:"))
        if Command != "Indlæs data" and Command != "Filtrer data" and Command != "Vis statistik" and Command != "Afslut":
            raise NameError
        break
    except  NameError:
        print("Dette input er ikke gyldigt. Tjek evt. for stavefejl og prøv igen.")
    except ValueError:
        print("Dette input er ikke gyldigt. Input skal være tekst")

print(Command)
      

#https://www.geeksforgeeks.org/python-raise-keyword/#:~:text=Python%20raise%20Keyword%20is%20used,further%20up%20the%20call%20stack.