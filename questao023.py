numero = int(input("Digite um número: "))
primos = []
divisoes = 0
for numero in range(3, numero + 1):
    divisor = 0
    for i in range(1, numero + 1):
        divisoes += 1
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        primos.append(numero)

print('primos', primos)
print("divisoes", divisoes)