from funções import cabecalho, detectador_de_senhafraca
import json
def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def atualizar_usuarios():
    import json
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        usuarios = {}
        return usuarios

def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


usuarios = carregar_usuarios()
try:
    cabecalho("faça seu login")
    print("digite um dos três numeros para oq vc quer fazer\n"
                      "1- criar conta\n"
                      "2- para cadastrar uma conta\n"
                      "3- deletar sua conta")
    escolha = int(input())
    if escolha > 3 or escolha < 1:
        print("desculpe lhe descepcionar mas só ha 3 opções")
except ValueError:
    print("so validamos numeros inteiros")
match escolha:
    case 1:
            nome = input("Digite o nome do usuário: ")
            if nome in usuarios:
                print("Esse usuário já existe, tente outro")
            elif not nome:
                print("escreva o seu nome!")
            else:
                while True:
                    senha = input("Digite a senha do usuário: ")
                    if detectador_de_senhafraca(senha):
                        print("Sua senha é fraca, tente outra.")
                    else:
                        try:
                            usuarios[nome] = {"senha": senha, 'tentativas': 0}
                            salvar_usuarios(usuarios)
                            print("Cadastrado com sucesso!")
                        except KeyError:
                            print("usuario não existe")
                        try:
                            atualizar_usuarios()
                        except FileNotFoundError:
                            usuarios = {}
                            print("arquivo n existe")
                        break
    case 2:
            nome = str(input("digite o nome do seu usuario: "))
            if not nome:
                print("escreva o seu nome!")
            if nome in usuarios:
                senha = input("digite sua senha: ")
                if senha == usuarios[nome]['senha']:
                    print("logado com sucesso.")
                else:
                    while True:
                        senha = (input("digite sua senha: "))
                        if senha in usuarios[nome]['senha']:
                            print("logado com sucesso.")
                            break
                        else:
                            usuarios[nome]['tentativas'] += 1
                            if usuarios[nome]['tentativas'] == 2:
                                print("muitas tentativas, usuario bloqueado")
                                salvar_usuarios(usuarios)
                                break
            else:
                print("usuario nao existe")
    case 3:
        print("Muito bem iremos excluir sua conta, mas antes nos de seu usuario e senha")
        nome = str(input("digite o nome do seu usuario: "))
        if not nome:
            print("escreva o seu nome!")
        elif nome in usuarios:
            senha = input("digite sua senha: ")
            if senha == usuarios[nome]['senha']:
                print("processo concluido com sucesso.")
                del usuarios[nome]
                salvar_usuarios(usuarios)
            else:
                while True:
                    print("senha incorreta.")
                    senha = (input("digite sua senha: "))
                    if senha == usuarios[nome]['senha']:
                        print("processo concluido com sucesso.")
                    else:
                        usuarios[nome]['tentativas'] += 1
                        if usuarios[nome]['tentativas'] == 2:
                            print("muitas tentativas, usuario bloqueado")
                            break
        else:
            print("usuario nao existe")
