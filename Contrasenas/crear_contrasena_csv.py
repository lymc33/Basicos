#Importaciones
import csv

#Contenido

bdUsuarios=[["Nombre", "Contrasena"],["Luis","1234"],["Yair","5678"],["Luis_Yair","12345678"]]

#Crear CSV
archivo=open("contrasenas.csv","w")
with archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(bdUsuarios)
print("CSV exitoso")
