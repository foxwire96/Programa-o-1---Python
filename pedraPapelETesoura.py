"""Breno da Cunha , Matheus da Cunha , Milena"""
import random
escolhas = ['PEDRA','TESOURA','PAPEL']

def UsuarioEscolha():
    while True:
        escolha = input("Digite Pedra,Papel ou Tesoura: ").upper()
        if escolha in escolhas:
            return escolha

        print("Escreva apenas pedra, papel ou tesoura")


def ChecarVitoria(escolhaDoUsuario,escolhaDoComputador):

    if escolhaDoUsuario == escolhaDoComputador:
        return "Empate"
    elif escolhasPossiveis:
        return "Ganhou"
    else:
        return "Perdeu"



escolhaDoComputador = random.choice(escolhas)
escolhaDoUsuario = UsuarioEscolha()
escolhasPossiveis = (
        (escolhaDoUsuario == 'PEDRA' and escolhaDoComputador == 'TESOURA') or
        ( escolhaDoUsuario == 'PAPEL' and escolhaDoComputador == 'PEDRA') or
        (escolhaDoUsuario == 'TESOURA' and escolhaDoComputador == 'PAPEL')
    )


print(f"Sua escolha foi :{escolhaDoUsuario} ")
print(f"Escolha do pc :{escolhaDoComputador} ")

vencedor = ChecarVitoria(escolhaDoUsuario,escolhaDoComputador)

print(vencedor)



