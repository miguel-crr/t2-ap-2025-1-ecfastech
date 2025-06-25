numero=int(input('Digite o fatorial: '))
produto=1
while numero>0:
    produto*=numero
    numero-=1
print(produto)