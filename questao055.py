matriz=[[1,2,3],[4,5,6],[7,8,9]]
maior=0
menor=999
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j]>maior:
            maior=matriz[i][j]
        if matriz[i][j]<menor:
            menor=matriz[i][j]
print('Maior',maior)
print('Menor',menor)