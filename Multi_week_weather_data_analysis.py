import numpy as np
# Voy a definir la función que me va a calcular la media de las temperaturas en cada semana
def Average_temperature(temperature):
    suma = sum(temperature)     # Sumo todos los elementos de la lista
    count = len(temperature)    # Cuento los elementos de la lista
    Average = suma / count      # Divido ambos miembros y me da la media de temepratura para 1 semana

    return Average

temperatures = [
    [22,24,19,21,23,25,20],     # Semana 1
    [20,22,21,23,22,24,21],     # Semana 2
    [23,21,20,22,24,25,23]      # Semana 3
]
changes = ([],[])
# Voy a crear un bucle while para que me de los datos que necesito de cada semana
i = 0
while i <= 2:    
    print(f"La temperatura de la semana {i+1} es: {Average_temperature(temperatures[i])}")
# Ahora voy a hacer un bucle que me de el valor máximo de temperatura por semana
    max = 0
    for valor in temperatures[i]:
        if valor > max:
            max = valor
            
    print(f"El día más caluroso de la semana {i+1} ha sido el día 6 con {max} grados")
# Con este bucle voy a comprobar que la tempratura de cada día este entre 20 y 25 grados
    j = 0
    for data in temperatures[i]:
        if temperatures[i][j] <= 25 and temperatures[i][j] >= 20:
            j = j+1
    if j == 7:
        print(f"La semana {i+1} ha tenido temepraruras entre 20 y 25 grados")
# Ahora voy a hacer una tabla con los cambios de la temepratura entre días
    z = 0
    for list in temperatures[i]:
        if list == temperatures[i][0]:
            changes[i][0] = 0
        else:
            changes[i][z] = temperatures[i][z] - temperatures[i][z-1]
        z = z+1
    print(changes[i]) 
    
    

    i = i+1
