numero = int(input("Fatorial de:"))

fatorial = 1
contador = numero

print(str(numero) + "! =", end=" ")

while contador > 0:
    print(contador, end="")
    fatorial = fatorial * contador
    contador = contador - 1
    if contador > 0:
        print(" . ", end=" ")
    else:
        print(" = ", end="")

print(fatorial)