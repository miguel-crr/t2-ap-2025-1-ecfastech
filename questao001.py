n=int(input('Digite um valor entre 0 e 10:'))
while n<0 or n>10:
    print('Valor invalido',n)
    n=int(input('Digite um valor entre 0 e 10:'))
print('Valor valido',n)