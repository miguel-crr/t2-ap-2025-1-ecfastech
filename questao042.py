intervalo1 = 0  
intervalo2 = 0 
intervalo3 = 0  
intervalo4 = 0  

while True:
    numero = int(input("Digite um número positivo (ou negativo para parar): "))

    if numero < 0:
        break

    if numero >= 0 and numero <= 25:
        intervalo1 = intervalo1 + 1
    elif numero >= 26 and numero <= 50:
        intervalo2 = intervalo2 + 1
    elif numero >= 51 and numero <= 75:
        intervalo3 = intervalo3 + 1
    elif numero >= 76 and numero <= 100:
        intervalo4 = intervalo4 + 1

print("Quantidade no intervalo de 0 a 25:", intervalo1)
print("Quantidade no intervalo de 26 a 50:", intervalo2)
print("Quantidade no intervalo de 51 a 75:", intervalo3)
print("Quantidade no intervalo de 76 a 100:", intervalo4)
