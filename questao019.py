quantidade=int(input('Digite quantos numeros deseja:'))
numero=int(input('Digite o numero entre 0 e 1000:'))
if numero<=1000 and numero>=0:
    menor=maior=soma=numero
    for i in range(quantidade-1):
        numero=int(input('Digite o numero:'))
        if numero<=1000 and numero>=0:
            soma+=numero
            if menor>numero:
                menor=numero
            if numero>maior:
                maior=numero
    print(soma, menor, maior)
else:
    print('Numero fora do intervalo')