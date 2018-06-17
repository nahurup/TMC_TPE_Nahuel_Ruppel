import random
from variables import *

def probar_probabilidad1():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidad:

       perdidos += 1

   else:

      noperdidos += 1


for i in range(0,pruebas):
    while i < numpaquetes:
     probar_probabilidad1()
     i += 1

print("Despues de {0} pruebas y {1} paquetes en cada una, hubo {2} perdidos y {3} no perdidos".format(pruebas, numpaquetes,perdidos,noperdidos))

promedioperdidos = perdidos / pruebas
promedionoperdidos = noperdidos / pruebas

""" 1 """
print("1) Hubo un promedio de {0} paquetes perdidos y {1} no perdidos calculado entre {2} pruebas".format(promedioperdidos, promedionoperdidos, pruebas))
perdidos = 0
noperdidos = 0

def probar_probabilidadA():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidadA:

       perdidos += 1

   else:

      noperdidos += 1


for i in range(0,pruebas):
    while i < numpaquetes:
     probar_probabilidadA()
     i += 1