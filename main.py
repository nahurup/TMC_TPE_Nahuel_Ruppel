import random
import numpy as np
from variables import *

def probar_probabilidad1():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidad:

       perdidos += 1

   else:

      noperdidos += 1


for i in range(0,pruebas10):
    while i < numpaquetes:
     probar_probabilidad1()
     i += 1

print("Despues de {0} pruebas y {1} paquetes en cada una, hubo {2} perdidos y {3} no perdidos".format(pruebas10, numpaquetes,perdidos,noperdidos))

promedioperdidos = perdidos / pruebas10
promedionoperdidos = noperdidos / pruebas10

print("1) Hubo un promedio de {0} paquetes perdidos y {1} no perdidos calculado entre {2} pruebas".format(promedioperdidos, promedionoperdidos, pruebas10))
print("")
perdidos = 0
noperdidos = 0

def probar_probabilidadA():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidadA:

       perdidos += 1

   else:

      noperdidos += 1


for i in range(0,pruebas10):
    while i < numpaquetes:
     probar_probabilidadA()
     i += 1
    perdidosA.append(perdidos)
    perdidos = 0



def probar_probabilidadB():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidadB:

       perdidos += 1

   else:

      noperdidos += 1


for i in range(0,pruebas15):
    while i < numpaquetes:
     probar_probabilidadB()
     i += 1
    perdidosB.append(perdidos)
    perdidos = 0



def probar_probabilidadC():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidadC:

       perdidos += 1

   else:

      noperdidos += 1


for i in range(0,pruebas15):
    while i < numpaquetes:
     probar_probabilidadC()
     i += 1
    perdidosC.append(perdidos)
    perdidos = 0

print(perdidosA)
print(perdidosB)
print(perdidosC)

maxABC.append(max(perdidosA))
maxABC.append(max(perdidosB))
maxABC.append(max(perdidosC))

print(maxABC)

probC = 0,1

while abs(probC - p_anterior) > epsilon1 or pruebas10 < 10:
    while i < numpaquetes:
        probar_probabilidadC()
        i+=1
    probC= perdidos / noperdidos
    p_anterior = probC

print(probC)



