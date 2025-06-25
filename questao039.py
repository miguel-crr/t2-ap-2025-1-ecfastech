maisAlto = 0
numeroMaisAlto = 0

maisBaixo = 9999
numeroMaisBaixo = 0

contador = 1
while contador <= 10:
    print("Digite o número do aluno", contador)
    numeroAluno = int(input())

    print("Digite a altura do aluno", contador, "em cm")
    altura = int(input())

    if altura > maisAlto:
        maisAlto = altura
        numeroMaisAlto = numeroAluno

    if altura < maisBaixo:
        maisBaixo = altura
        numeroMaisBaixo = numeroAluno

    contador = contador + 1

print("Aluno mais alto:", numeroMaisAlto)
print("Altura:",maisAlto, "cm")

print("Aluno mais baixo:",numeroMaisBaixo)
print("Altura:",maisBaixo, "cm")