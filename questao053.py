matriz=[[2,4,2],[7,5,2],[8,2,1]]
contador=0
n=2
for linha in matriz:
    for valor in linha:
        if valor==n:
            contador+=1
print(contador)