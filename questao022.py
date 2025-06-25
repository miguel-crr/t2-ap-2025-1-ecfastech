numero=int(input('Digite um numero: '))
divisores=[]
if numero<2:
    print('Nao é primo')
else:
    divisor=0
    for i in range(1,numero+1):
        if numero%i==0:
            divisor+=1
            divisores.append(i)
    if divisor==2:
        print('É primo')
    else:
        print('Nao é primo')
        print(divisores)