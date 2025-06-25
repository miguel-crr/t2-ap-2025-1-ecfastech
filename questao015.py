termo=int(input('Digite ate o termo que quiser:'))
a=1
b=0
soma=0
for i in range(termo):
    soma=a+b
    a=b
    b=soma
    print(soma)