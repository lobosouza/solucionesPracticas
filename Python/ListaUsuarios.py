'''Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo)
 no repetidas, guardarlos en una lista y mostrarlos

Intentos: 

i = "Fin"
lista = []

while i != "Fin":
    i = input("Igrese nombre de usuario. Ingrese Fin si desea terminar ")
    lista.append(i)

# como crear una lista con los usuarios ingresados?
print(lista)


lista = []

while True:
    i = input("Ingrese nombre de usuario. Ingrese 'Fin' si desea terminar: ")
    if i == "fin":
        break
    lista.append(i)

print("Lista de usuarios ingresados:", lista)'''

lista = []

while True:
    valor = input("Ingrese nombre de usuario. Ingrese Fin si desea terminar: ")
    if valor == "Fin":
        break
    lista.append(valor)
print("lista de usarios ingresados", lista)

# Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

del lista[3]
lista.pop()
lista.sort()
print(lista)