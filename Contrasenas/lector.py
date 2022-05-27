#Importaciones

import csv
import pandas as pd
from tkinter import messagebox


#Lector de CSV

# Directo con csv
 
##arreglo=[]
##with open("contrasenas.csv") as contrasenas:
##    lector = csv.reader (contrasenas,
##                         delimiter=",",
##                         quotechar=",",
##                         quoting=csv.QUOTE_MINIMAL)
##    for renglon in lector:
##        if (len(renglon)!=0):
##            arreglo.append(renglon)
##print(arreglo)
##print(arreglo[1:])
##print(arreglo[1:][:])
##print(arreglo[1:][:][:1])

# Agregar csv
# arreglo2= []
# for i in range (len(arreglo)):
#     edad=random.randint(20,35)
#     if (i==0):
#         arreglo2.append(["Nombre",
#                          "Contraseña",
#                          "Edad"])
#     else:
#         arreglo[i].append(edad)
#         ls=arreglo[i]
#         arreglo2.append(ls)
# print(arreglo2)


# CSV a pandas

df = pd.read_csv("contrasenas.csv")
Nombre_contrasenas=(df.loc[:]["Nombre"])
Contrasena_contrasenas=(df.loc[:]["Contrasena"])

#Input

Nombre_sistema= input("Ingrese Nombre: ")
# Contrasena_sistema= input("Ingrese Contraseña: ")


#Comprobador

# Comprobador_nombre = df.loc[df['Nombre'].str.contains(Nombre_sistema, case=False)]
# Comprobador_nombre = (df.loc[df['Nombre'] == Nombre_sistema]
# print(Comprobador_nombre)
# print(type(Comprobador_nombre))

#Alertas

# if (Comprobador_nombre = True):
#     print("cool")
# else:
#     print("bad")

# if (Comprobador_nombre == True):
#     print("cool")
# else:
#     print("bad")

# else:
#     print("looser")
    





# Mensajes

# showinfo()
# showwarning()
# showerror()

# askquestion()
# askyesno()
# askokcancel()
# askoknocancel()

# \n Salto de linea

# valor=messagebox.askokcancel(message="Esto es una \n prueba de información", title="ventana")
# print(valor)