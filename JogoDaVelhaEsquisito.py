"""Breno da Cunha , Matheus da Cunha , Milena"""
tabuleiro = []
i = 0


def ImprimirTabuleiro():
    print()
    print('', tabuleiro[8], "|", tabuleiro[7], "|", tabuleiro[6])
    print("---|---|---")
    print('', tabuleiro[5], "|", tabuleiro[4], "|", tabuleiro[3])
    print("---|---|---")
    print('', tabuleiro[2], "|", tabuleiro[1], "|", tabuleiro[0])
    print()

    print('A Soma da Diagonal principal é ', soma_diagonal)


while i <= 8:
    numeros = input('Insira um número: ')
    try:
        numeros_int = int(numeros)
    except:
        print('Digite apenas números inteiros por favor.')
        continue

    tabuleiro.append(numeros_int)
    i += 1

soma_diagonal = tabuleiro[8] + tabuleiro[4] + tabuleiro[0]

ImprimirTabuleiro()