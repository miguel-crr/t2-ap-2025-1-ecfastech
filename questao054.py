matriz=[[1,2,3],[4,5,6],]
matriz2=[]
for i in range(len(matriz)):
    linha=[]
    for j in range(len(matriz)):
        linha.append(matriz[j][i])
    matriz2.append(linha)
print(matriz2)