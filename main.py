import random

perdidos = 0
noperdidos = 0
i = 0

viajes = 10
numpaquetes = 300
probabilidad = 12

def probar_probabilidad():

   global noperdidos
   global perdidos

   if random.randint(1,100) < probabilidad:

      print("Perdido")
      perdidos += 1

   else:

      print("No perdido")
      noperdidos += 1


for i in range(0,viajes):
    while i < numpaquetes:
     probar_probabilidad()
     i += 1

print("Despues de {0} viajes y {1} paquetes en cada uno, hubo {2} perdidos y {3} no perdidos".format(viajes, numpaquetes,perdidos,noperdidos))

promedioperdidos = perdidos / viajes
promedionoperdidos = noperdidos / viajes

print("Hubo un promedio de {0} paquetes perdidos y {1} no perdidos por mes en {2} viajes".format(promedioperdidos, promedionoperdidos, viajes))
