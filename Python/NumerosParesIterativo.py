'''Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
Nota: para saber si un número es par hacer i % 2 == 0)'''

n = int(input("Ingrese un número: "))

for i in range(n):
    if i % 2 == 0:
        print(i)
    