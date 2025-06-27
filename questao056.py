matriz=[]
linha=int(input('Linhas: '))
colunas=int(input('Colunas: '))
elemento=0
for i in range(linha):
    novaLinha=[]
    for j in range(colunas):
        elemento = i * j
        novaLinha.append(elemento)
    matriz.append(novaLinha)
print(matriz)