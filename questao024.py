qtd=int(input('Digite a quantidade de notas: '))
media=0
for i in range(qtd):
    notas=float(input('Digite a nota: '))
    media+=notas
media=media/qtd
print(media)