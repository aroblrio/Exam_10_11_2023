name = str(input("Introduce tu nombre: ", ))
age = int(input("Introduce tu edad: ", ))
while age < 0:
    age = int(input("No puedes tener un edad negativa, prueba otra vez: ",))
year = 2023 - age
year = year + 100
print (f"{name}, cumplirás 100 años en el año {year}")