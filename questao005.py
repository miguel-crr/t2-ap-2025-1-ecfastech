while True:

    pop1=int(input('Digite a populaçao 1:'))
    tax1=int(input('Digite a taxa de crescimento da populaçao 1: '))
    pop2=int(input('Digite a populaçao 2:'))
    tax2=int(input('Digite a taxa de crescimento da populaçao 2: '))
    tax1=tax1/100 + 1
    tax2=tax2/100 + 1

    while pop1<0 or pop2<0:
        print('populaçao invalida')
        pop1=int(input('Digite a populaçao 1:'))
        pop2=int(input('Digite a populaçao 2:'))

    while tax1<1 or tax2<1:
        print('Taxa invalida')
        tax1=int(input('Digite a taxa de crescimento da populaçao 1: '))
        tax2=int(input('Digite a taxa de crescimento da populaçao 2: '))

    while pop1>=pop2:
        print('A populaçao 1 ja é igual ou maior a 2')
        pop1=int(input('Digite a populaçao 1:'))
        pop2=int(input('Digite a populaçao 2:'))
        
    anos=0

    while pop1<pop2:
        pop1=pop1*tax1
        pop2=pop2*tax2
        anos+=1

    print(anos,'anos')

    repetir = input("Deseja repetir a operação? (s/n): ")
    
    if repetir.lower() != 's':
        print("Programa encerrado.")
        break