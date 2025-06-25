gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

maiorAcerto = 0
menorAcerto = 10
somaNotas = 0
totalAlunos = 0

while True:
    acertos = 0
    print("Responda as 10 questões (A, B, C, D ou E)")

    for i in range(10):
        resposta = input("Digite a resposta da questão " + str(i + 1) + ": ").upper()
        if resposta == gabarito[i]:
            acertos = acertos + 1

    print("Total de acertos:", acertos)
    print("Nota do aluno:", acertos)

    if acertos > maiorAcerto:
        maiorAcerto = acertos

    if acertos < menorAcerto:
        menorAcerto = acertos

    somaNotas = somaNotas + acertos
    totalAlunos = totalAlunos + 1

    outro = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()
    if outro != 'S':
        break

mediaNotas = somaNotas / totalAlunos

print("Maior número de acertos:", maiorAcerto)
print("Menor número de acertos:", menorAcerto)
print("Total de alunos que utilizaram o sistema:", totalAlunos)
print("Média das notas da turma:", mediaNotas)
