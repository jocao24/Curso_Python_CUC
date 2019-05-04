# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#Ejercicio Mayor de edad
"""
print("Digite su edad")
edad = input();
edad = int(edad);

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
"""
#print("Usted es mayor de edad") if edad >= 18 else print("Usted es menor de edad")

#Arrays

v = ["Hola","Mundo", 4, 3.4, True, ["Otro", "Array", "Dentro"]]
v2 = ["Hola", "Mundo"]
v3 = range(1,200)  ##inicia el array desde 1 hasta 199

"""
print(v3)
for x in v3:
    print(x)

print(v2[1])
"""

v2[1] = ["Jocao24"]
v2.remove("Hola")
"""
v.pop()
v.pop(4) #elimino el elemento número 4 del vector v

v.insert(1,"Skate") # inserto en la posición 1 la palabra Skate
"""
#v.clear()    #elimina todos los elementos del vector

#v.index('Skate')

a = [4,6,2,3,7,8]
res = 8 in a
print(res)

aux = v[5]
aux = aux[0]
print(aux)

v = v[2:5] #defino un rango desde el cual se recorrerá el vector con el for
for x in v:
    print(x)

#Sumatoria de los números del 1 al 100

z = range(0,101)
for y in z[:101]:
    suma = suma+y
    
print (suma)












