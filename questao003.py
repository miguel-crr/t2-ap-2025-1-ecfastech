nome=input('Digite seu nome:')

while not(len(nome)>3):
    print('Nome invalido')
    nome=input('Digite um nome com mais de 3 caracteres:')

idade=int(input('Digite sua idade:'))

while idade<0 or idade>150:
    print('Idade invalida')
    idade=int(input('Digite uma idade valida:'))

salario=float(input('Digite seu salario:'))

while not(salario>0):
    print('Salario invalido')
    salario=float(input('Digite um salario valido:'))

sexo=input('Digite seu sexo "f" ou "m" :').lower()

while not(sexo=='m' or sexo=='f'):
    print('Sexo invalido')
    sexo=input('Digite seu sexo "f" ou "m" :').lower()

estado=input('Digite seu estado civil "s", "c", "v" ou "d" :').lower()
lista_estado=['s','c','v','d']

while not(estado in lista_estado):
    print('Estado civil invalido')
    estado=input('Digite seu estado civil "s", "c", "v" ou "d" :').lower()
    
print('Informaçoes validas')