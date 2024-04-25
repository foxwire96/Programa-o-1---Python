"""Breno da Cunha , Matheus da Cunha , Milena"""
def AnalisarSenhas():
    senha = input("Digite a senha: ")

    tamanho_senha = len(senha)
    versao_maiuscula = senha.upper()
    versao_minuscula = senha.lower()

    print(f"Tamanho da senha: {tamanho_senha}")
    print(f"Versão maiúscula: {versao_maiuscula}")
    print(f"Versão minúscula: {versao_minuscula}")

AnalisarSenhas()