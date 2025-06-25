while True:
    media=divisor=0
    pergunta=input('Caso nao haja temperatura digite "N" ').upper()
    temperatura=float(input('Digite a temperatura:'))
    maior=menor=temperatura
    if pergunta=='N':
        break
    else:
        media+=temperatura
        divisor+=1
        if menor>temperatura:
            menor=temperatura
        if maior<temperatura:
            maior=temperatura
print('Maior',maior)
print('Menor',menor)
print('Media',media)