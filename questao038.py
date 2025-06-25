salarioInicial = float(input("Digite o salário inicial do funcionário em 1995: "))
salario = salarioInicial
anoContratacao = 1995
anoAtual = 2025

percentualAumento = 1.5 / 100 

for ano in range(1996, anoAtual + 1):
    salario = salario + salario * percentualAumento
    percentualAumento = percentualAumento * 2

print("Salário atual em", anoAtual, ": R$ ", round(salario, 2))