N = int(input("Digite o número de termos N: "))
H = 0
for i in range(1, N + 1):
    H = H + 1 / i
print("Valor de H com", N, "termos:", H)
