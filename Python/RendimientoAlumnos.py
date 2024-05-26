'''
Verificar el promedio de los alumnos. Se conoce cuántos alumnos han rendido.
Promedio elevado > 8
6 < Promedio aceptable < 8 
Promedio bajo < 6
n = nro de alumnos 

promedio = totalnotas/n
'''

n = int(input("Ingrese cuántos alumnos rendieron: "))

for i in range(n):
    nota = int(input("Ingrese la nota del estudiante: "))

# cómo sumo las notas ingresadas para luego realizar el promedio?
promedio = totalnotas/n

if promedio >=8:
    print("El promedio es elevado")
elif promedio > 6 and promedio < 8:
    print("El promedio es aceptable")
elif promedio < 6:
    print("El promedio es bajo")