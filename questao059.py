texto=input('Digite uma frase: ')
vogal='aeiou'
vogais=conso=0
for letra in texto:
    if letra in vogal:
        vogais+=1
    else:
        conso+=1
print('Vogais:',vogais)
print('Consoantes:',conso)