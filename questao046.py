while True:
    nomeAtleta = input("Digite o nome do atleta (ou pressione Enter para encerrar): ")

    if nomeAtleta == "":
        break

    saltos = []

    salto1 = float(input("Digite a distância do primeiro salto: "))
    saltos.append(salto1)

    salto2 = float(input("Digite a distância do segundo salto: "))
    saltos.append(salto2)

    salto3 = float(input("Digite a distância do terceiro salto: "))
    saltos.append(salto3)

    salto4 = float(input("Digite a distância do quarto salto: "))
    saltos.append(salto4)

    salto5 = float(input("Digite a distância do quinto salto: "))
    saltos.append(salto5)

    print("Atleta:", nomeAtleta)
    print("Primeiro Salto:", salto1, "m")
    print("Segundo Salto:", salto2, "m")
    print("Terceiro Salto:", salto3, "m")
    print("Quarto Salto:", salto4, "m")
    print("Quinto Salto:", salto5, "m")

    melhorSalto = max(saltos)
    piorSalto = min(saltos)

    print("Melhor salto:", melhorSalto, "m")
    print("Pior salto:", piorSalto, "m")

    saltos.remove(melhorSalto)
    saltos.remove(piorSalto)

    media = sum(saltos) / len(saltos)

    print("Média dos demais saltos:", media, "m")
    print("Resultado final:")
    print(nomeAtleta + ":", media, "m")