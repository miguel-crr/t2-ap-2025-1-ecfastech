print("Lojas Tabajara")

while True:
    total = 0
    produto = 1

    preco = 1
    while preco != 0:
        print("Produto", produto, ": R$")
        preco = float(input())
        if preco != 0:
            total = total + preco
            produto = produto + 1

    print("Total: R$")
    print(total)

    print("Dinheiro: R$")
    dinheiro = float(input())

    troco = dinheiro - total
    print("Troco: R$")
    print(troco)
