qtd=int(input('Quantidade de CDs: '))
total=0
for i in range(qtd):
    valor=float(input('Valor do CD: '))
    total+=valor
media=total/qtd
print('Total: ', total)
print('Media: ', media)