numero = int(input("Vou montar a tabuada de qual número? "))
inicio = int(input("Começando por: "))
fim = int(input("Terminando em: "))

if fim < inicio:
    print("Erro! O valor final não pode ser menor que o valor inicial.")
else:
    contador = inicio
    while contador <= fim:
        resultado = numero * contador
        print(numero, "X", contador, "=", resultado)
        contador = contador + 1
