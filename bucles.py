print("bucles")
def generar_pares(limite):
    for i in range(limite):
        if i % 2 == 0:
            yield i

for par in generar_pares(10):
    print(par) 