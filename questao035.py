limite = int(input("Informe um número inteiro:"))

numero = 2 

while numero <= limite:
    contador = 1
    divisores = 0

    while contador <= numero:
        if numero % contador == 0:
            divisores = divisores + 1
        contador = contador + 1

    if divisores == 2:
        print(numero)

    numero = numero + 1
