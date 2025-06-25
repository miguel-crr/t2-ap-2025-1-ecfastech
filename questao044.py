votosJose = 0
votosJoao = 0
votosMaria = 0
votosAna = 0
votosNulo = 0
votosBranco = 0

print("1 - José")
print("2 - João")
print("3 - Maria")
print("4 - Ana")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("Digite 0 para encerrar\n")

while True:
    voto = int(input("Digite o código do voto: "))

    if voto == 0:
        break
    elif voto == 1:
        votosJose = votosJose + 1
    elif voto == 2:
        votosJoao = votosJoao + 1
    elif voto == 3:
        votosMaria = votosMaria + 1
    elif voto == 4:
        votosAna = votosAna + 1
    elif voto == 5:
        votosNulo = votosNulo + 1
    elif voto == 6:
        votosBranco = votosBranco + 1

totalVotos = votosJose + votosJoao + votosMaria + votosAna + votosNulo + votosBranco

print("Total de votos para José:", votosJose)
print("Total de votos para João:", votosJoao)
print("Total de votos para Maria:", votosMaria)
print("Total de votos para Ana:", votosAna)
print("Total de votos nulos:", votosNulo)
print("Total de votos em branco:", votosBranco)

if totalVotos > 0:
    percentualNulo = (votosNulo / totalVotos) * 100
    percentualBranco = (votosBranco / totalVotos) * 100

    print("Percentual de votos nulos sobre o total de votos:", percentualNulo, "%")
    print("Percentual de votos em branco sobre o total de votos:", percentualBranco, "%")
else:
    print("Nenhum voto foi registrado.")
