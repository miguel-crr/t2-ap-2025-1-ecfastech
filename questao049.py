n = int(input("Digite a quantidade de termos da série: "))
soma = 0
denominador = 1
for i in range(1, n + 1):
    termo = i / denominador
    print(str(i) + "/" + str(denominador))
    soma = soma + termo
    denominador = denominador + 2
print("Soma da série:", soma)
