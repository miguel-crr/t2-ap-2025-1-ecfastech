numero1=int(input('Digite um numero:'))
numero2=int(input('Digite outro numero maior que o primeiro:'))
soma=0
while numero1<(numero2-1):
    numero1+=1
    soma+=numero1
print(soma)