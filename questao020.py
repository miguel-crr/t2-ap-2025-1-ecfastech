numero=int(input('Digite um numero menor que 16: '))
produto=1
if numero<16:
    while numero>0:
        produto*=numero
        numero-=1
    print(produto)
else:
    print('Fora do intervalo')