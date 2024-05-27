'''Guardar en una tupla los primeros n números pares. i % 2 == 0
El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.'''

tupla = ()

n = list(tupla)

x = int(input("Ingrese un número: "))

if x % 2 == 0:
    n.append(x)
tupla = tupla(n)
print(tupla)