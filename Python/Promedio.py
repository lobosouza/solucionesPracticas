'''
Realizar el promedio de notas de 5 materias
1. Datos
Nota_Materia -> float
Promedio -> float
2. ResultadoPromedio  = (Nota_Materia1 + Nota_Materia2 + Nota_Materia3 + Nota_Materia4 + Nota_Materia5)/5 -> float '''

nota1 = float(input("Ingrese Nota 1: "))
nota2 = float(input("Ingrese Nota 2: "))
nota3 = float(input("Ingrese Nota 3: "))
nota4 = float(input("Ingrese Nota 4: "))
nota5 = float(input("Ingrese Nota 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print("Tu promedio es: ",promedio)
