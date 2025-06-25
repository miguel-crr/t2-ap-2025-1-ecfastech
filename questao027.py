turmas=int(input('Quantidade de turmas: '))
media=0
for i in range(turmas):
    alunos=int(input('Quantidade de alunos: '))
    while alunos>40:
        alunos=int(input('corrija a quantidade de alunos: '))
    else:
        media+=alunos
media/=turmas
print(media)