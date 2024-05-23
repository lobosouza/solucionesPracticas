NGanados = int(input("Nro. de partidos ganados"))

NPerdidos = int(input("Nro. de partidos perdidos"))

NEmpatados = int(input("Nro. de partidos empatados"))

PGanados = NGanados*3

PEmpatados = NEmpatados*1

PPerdidos = NPerdidos*0

PuntosTotales = PGanados + PEmpatados + PPerdidos

print("Los puntos de tu equipo en este campeonato es: ", PuntosTotales)
