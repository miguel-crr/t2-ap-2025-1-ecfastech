numero = int(input("Digite um número inteiro:"))

divisores = 0
contador = 1

while contador <= numero:
    if numero % contador == 0:
        divisores = divisores + 1
    contador = contador + 1

if divisores == 2:
    print("É um número primo.")
else:
    print("Não é um número primo.")
