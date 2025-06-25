preço=float(input('Preço do pao: '))
print('Panificadora Pão de Ontem - Tabela de preços')
for i in range(1,51,1):
    valor=preço*i
    print(i,'-',valor)