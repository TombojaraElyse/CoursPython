# -*-coding:utf-8 -*
#0
# import os


annee= input("Saisissez une année supérieure à 0 : ")
try:
    annee= int(annee) # Conversion de l'année
    if annee <= 0:
       print('NON')

except ValueError:
    print("La valeur saisie est invalide")

else:
    print(" Année : ", annee)

finally:
    print("FIN")
#os.system("pause")