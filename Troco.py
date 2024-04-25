"""Breno da Cunha, Matheus Da Cunha , Milena"""
def CalcularTroco(custo, valorPago):
    troco = valorPago - custo
    notas = [20, 10, 5, 2, 1]
    numeroDeNotas = []

    for nota in notas:
        qtdNotas = troco // nota
        if qtdNotas > 0:
            troco %= nota
        numeroDeNotas.append(qtdNotas)

    return notas, numeroDeNotas


custoDoItem = int(input("Digite o custo do item: "))
valorPago = int(input("Digite o valor pago: "))

notasTroco, quantidadeTroco = CalcularTroco(custoDoItem, valorPago)

print("Troco total: ")
for i in range(len(notasTroco)):
    if quantidadeTroco[i] > 0:
        print(f"{quantidadeTroco[i]} notas de R$ {notasTroco[i]}", end=". ")
