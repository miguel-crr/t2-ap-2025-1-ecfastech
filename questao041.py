valorDivida = float(input("Digite o valor da dívida: "))

print("Valor da Dívida", "Valor dos Juros", "Quantidade de Parcelas", "Valor da Parcela")

quantidadeParcelas = 1
juros = 0

while quantidadeParcelas <= 12:
    if quantidadeParcelas == 1:
        juros = 0
    elif quantidadeParcelas == 3:
        juros = 10
    elif quantidadeParcelas == 6:
        juros = 15
    elif quantidadeParcelas == 9:
        juros = 20
    elif quantidadeParcelas == 12:
        juros = 25
    else:
        quantidadeParcelas = quantidadeParcelas + 1

    valorJuros = valorDivida * (juros / 100)
    valorTotal = valorDivida + valorJuros
    valorParcela = valorTotal / quantidadeParcelas

    print("R$", valorTotal, "     ", valorJuros, "           ", quantidadeParcelas, "                  R$", valorParcela)

    quantidadeParcelas = quantidadeParcelas + 1
