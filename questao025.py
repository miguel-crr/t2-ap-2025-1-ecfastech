qtd=int(input('Digite a quantidade de pessoas: '))
media=0
for i in range(qtd):
    idade=int(input('Digite a idade: '))
    media=+idade
media=media/qtd
print(media)
if media<=25 and media>0:
    print('jovem')
elif media>25 and media<=60:
    print('adulta')
elif media>60:
    print('idosa')