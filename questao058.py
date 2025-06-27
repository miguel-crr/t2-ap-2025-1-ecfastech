matriz=[[1,2,3],[4,5,6],[7,8,9]]
matriz2=[]
for i in range(len(matriz)-1,-1,-1):
    matriz2.append(matriz[i])
print(matriz2)