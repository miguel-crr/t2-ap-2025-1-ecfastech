matriz=[[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
linhas  =len(matriz)
coluna=len(matriz[0])
quadrada=True
for linha in matriz:
    if len(linha)!=coluna:
        quadrada=False
        break
if quadrada and linhas==coluna:
    print(True)
else:
    print(False)