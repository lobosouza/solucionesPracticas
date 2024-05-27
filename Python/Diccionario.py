# Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.


diccionario = {}

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dni = int(input("ingrese su dni: "))
fecha_nacimiento = int(input("ingrese su fecha de nacimiento: "))
mail = input("ingrese su mail: ")

diccionario = {
    "nombre": nombre,
    "apellido": apellido,
    "dni": dni,
    "fecha_nacimiento": fecha_nacimiento,
    "mail": mail
}


print(diccionario)