print("condicionales")
notas = [7, 8, 9, 10]

if all(nota >= 6 for nota in notas):
    print("Todas las notas son aprobatorias")
elif any(nota < 6 for nota in notas):
    print("Hay al menos una nota reprobatoria")
