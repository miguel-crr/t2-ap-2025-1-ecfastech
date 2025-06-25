totalGeral = 0

print("Cardápio:")
print("100 - Cachorro Quente - R$ 1,20")
print("101 - Bauru Simples   - R$ 1,30")
print("102 - Bauru com Ovo    - R$ 1,50")
print("103 - Hambúrguer       - R$ 1,20")
print("104 - Cheeseburguer    - R$ 1,30")
print("105 - Refrigerante     - R$ 1,00")
print("Digite um código fora do cardápio para encerrar.\n")

while True:
    codigo = int(input("Digite o código do produto: "))

    if codigo < 100 or codigo > 105:
        break

    quantidade = int(input("Digite a quantidade desejada: "))

    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1.00

    totalItem = preco * quantidade
    totalGeral = totalGeral + totalItem

    print("Valor do item:", totalItem)

print("Total geral do pedido:", totalGeral)