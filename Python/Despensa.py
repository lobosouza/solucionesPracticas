''' 
En una despensa se plantea las siguientes condiciones para obtener descuentos:

Unidades < 12 
Jubilados → 10% = 0.1 

Unidades ≥ 12 → Descuento 10%
Jubilados = 10% = 20% =0.2
NoJubilados =  10% = 0.1 

Unidades ≥ 24 → Descuento 15% 
Jubilados = 10%
DescuentoTotal Jubilados = 25% = 0.25
NoJubilados = 15% = 0.15

Entradas:
Unidades int
Jubilados int (0 o 1)

Salidas
MontoParcial = Unidades*1000
MontoTotal = MontoParcial - MontoParcial*Descuento
'''

Jubilado = int(input("Ingrese 1 si es Jubilado. Ingrese 0 si no es Jubilado: "))
Unidades = int(input("Ingrese unidades compradas: "))
MontoParcial = Unidades*1000

if Unidades < 12:
    if Jubilado == 1:
        MontoTotal = MontoParcial-(MontoParcial*0.1)
    else:
        MontoTotal = MontoParcial
    
elif Unidades >=12 and Unidades <24:
    if Jubilado == 1:
        MontoTotal = MontoParcial-(MontoParcial*0.2)
    else:
        MontoTotal = MontoParcial-(MontoParcial*0.1)
    
elif Unidades >= 24:
    if Jubilado == 1:
        MontoTotal = MontoParcial-(MontoParcial*0.25)
    else:
        MontoTotal = MontoParcial-(MontoParcial*0.15)

print("El monto total es: ", MontoTotal)