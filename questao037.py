maisAlto = 0
codigoAlto = 0

maisBaixo = 999
codigoBaixo = 0

maisGordo = 0
codigoGordo = 0

maisMagro = 999
codigoMagro = 0

somaAlturas = 0
somaPesos = 0
quantidadeClientes = 0

while True:
    codigo = int(input("Digite o codigo do cliente (0 para encerrar): "))
    if codigo == 0:
        break

    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em kg): "))

    somaAlturas = somaAlturas + altura
    somaPesos = somaPesos + peso
    quantidadeClientes = quantidadeClientes + 1

    if altura > maisAlto:
        maisAlto = altura
        codigoAlto = codigo

    if altura < maisBaixo:
        maisBaixo = altura
        codigoBaixo = codigo

    if peso > maisGordo:
        maisGordo = peso
        codigoGordo = codigo

    if peso < maisMagro:
        maisMagro = peso
        codigoMagro = codigo

if quantidadeClientes > 0:
    mediaAltura = somaAlturas / quantidadeClientes
    mediaPeso = somaPesos / quantidadeClientes

    print("\n--- RESULTADOS DO CENSO ---")
    print("Cliente mais alto:", codigoAlto, "- Altura:", maisAlto, "m")
    print("Cliente mais baixo:", codigoBaixo, "- Altura:", maisBaixo, "m")
    print("Cliente mais gordo:", codigoGordo, "- Peso:", maisGordo, "kg")
    print("Cliente mais magro:", codigoMagro, "- Peso:", maisMagro, "kg")
    print("Media das alturas:", round(mediaAltura, 2), "m")
    print("Media dos pesos:", round(mediaPeso, 2), "kg")
else:
    print("Nenhum cliente foi registrado.")
