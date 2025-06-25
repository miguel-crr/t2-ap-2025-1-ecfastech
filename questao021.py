numero=int(input('Digite um numero: '))
if numero<2:
    print('Nao é primo')
else:
    divisor=0
    for i in range(1,numero+1):
        if numero%i==0:
            divisor+=1
    if divisor==2:
        print('É primo')
    else:
        print('Nao é primo')