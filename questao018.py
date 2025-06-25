quantidade=int(input('Digite quantos numeros deseja:'))
numero=int(input('Digite o numero:'))
menor=maior=soma=numero
for i in range(quantidade-1):
    numero=int(input('Digite o numero:'))
    soma+=numero
    if menor>numero:
        menor=numero
    if numero>maior:
        maior=numero
print(soma, menor, maior)