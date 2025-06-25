maiorIndice = -1
cidadeMaiorIndice = 0

menorIndice = 999999
cidadeMenorIndice = 0

somaVeiculos = 0
somaAcidentesMenos2000 = 0
quantidadeMenos2000 = 0

contador = 1
while contador <= 5:
    codigoCidade = int(input("Digite o código da cidade: "))
    numVeiculos = int(input("Digite o número de veículos de passeio (em 1999): "))
    numAcidentes = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))

    if numVeiculos != 0:
        indiceAcidentes = numAcidentes / numVeiculos
    else:
        indiceAcidentes = 0

    if indiceAcidentes > maiorIndice:
        maiorIndice = indiceAcidentes
        cidadeMaiorIndice = codigoCidade

    if indiceAcidentes < menorIndice:
        menorIndice = indiceAcidentes
        cidadeMenorIndice = codigoCidade

    somaVeiculos = somaVeiculos + numVeiculos

    if numVeiculos < 2000:
        somaAcidentesMenos2000 = somaAcidentesMenos2000 + numAcidentes
        quantidadeMenos2000 = quantidadeMenos2000 + 1

    contador = contador + 1

mediaVeiculos = somaVeiculos / 5

if quantidadeMenos2000 > 0:
    mediaAcidentesMenos2000 = somaAcidentesMenos2000 / quantidadeMenos2000
else:
    mediaAcidentesMenos2000 = 0

print("Cidade com maior índice de acidentes:", cidadeMaiorIndice)
print("Maior índice de acidentes:", maiorIndice)
print("Cidade com menor índice de acidentes:", cidadeMenorIndice)
print("Menor índice de acidentes:", menorIndice)
print("Média de veículos nas cinco cidades:", mediaVeiculos)
print("Média de acidentes nas cidades com menos de 2000 veículos:", mediaAcidentesMenos2000)