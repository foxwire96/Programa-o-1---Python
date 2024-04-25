"""Breno da Cunha , Matheus da Cunha , Milena"""
def ValidarSenha(senha):
    if len(senha) < 6 or len(senha) > 8:
        return False

    temNumero = False
    temMaiusculo = False

    if senha[0].isdigit():
        return False

    for char in senha:
        if char.isdigit():
            temNumero = True
        elif char.isupper():
            temMaiusculo = True

    return temNumero and temMaiusculo


senha = input("Digite a senha: ")

tamanho_senha = len(senha)
versao_maiuscula = senha.upper()
versao_minuscula = senha.lower()

print(f"Tamanho da senha: {tamanho_senha}")
print(f"Versão maiúscula: {versao_maiuscula}")
print(f"Versão minúscula: {versao_minuscula}")

if ValidarSenha(senha):
    print("Senha válida")
else:
    print("Senha inválida")
