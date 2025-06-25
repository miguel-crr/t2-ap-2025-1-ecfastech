impar=0
par=0
for i in range(1,11):
    numero=int(input('Digite um numero:'))
    if numero%2==0:
        par+=1
    else:
        impar+=1
print(par,'numeros pares e',impar,'numeros impares')