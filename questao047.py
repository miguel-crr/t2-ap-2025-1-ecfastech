nomeAtleta = input("Digite o nome do atleta: ")

notas = []

nota1 = float(input("Digite a nota do jurado 1: "))
notas.append(nota1)

nota2 = float(input("Digite a nota do jurado 2: "))
notas.append(nota2)

nota3 = float(input("Digite a nota do jurado 3: "))
notas.append(nota3)

nota4 = float(input("Digite a nota do jurado 4: "))
notas.append(nota4)

nota5 = float(input("Digite a nota do jurado 5: "))
notas.append(nota5)

nota6 = float(input("Digite a nota do jurado 6: "))
notas.append(nota6)

nota7 = float(input("Digite a nota do jurado 7: "))
notas.append(nota7)

print("Atleta:", nomeAtleta)

print("Nota:", nota1)
print("Nota:", nota2)
print("Nota:", nota3)
print("Nota:", nota4)
print("Nota:", nota5)
print("Nota:", nota6)
print("Nota:", nota7)

melhorNota = max(notas)
piorNota = min(notas)

notas.remove(melhorNota)
notas.remove(piorNota)

media = sum(notas) / len(notas)

print("Resultado final:")
print("Atleta:", nomeAtleta)
print("Melhor nota:", melhorNota)
print("Pior nota:", piorNota)
print("Média:", media)
