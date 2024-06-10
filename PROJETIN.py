# MENU DO PROJETO CINEMA
from registro_login import *
from funçõesAdm import *
from funcoesUsuarios import *
from Menus import *
card = None
cs = None
todos_logins = {"c": ["caze1", "1", 1], "guilherme1@gmail.com":["guilherme1","12345", 1], "normal":["usuario","1",2]}
dicionario_creditos = {}
dicionario_filmes = {"aquaman":["5","16:30",15,2]}
ganhos = {"ganhos":[0,0]}
while True:
    print("---------MENU CINEMA----------\n\n1: Fazer Login\n2: Se Registrar\n3: Entrar como visitante\n4: Sair")
    op = input('\nDigite a opção desejada:')
    if op != "1" and op != "2" and op != "3" and op != "4":
        print("\n""Caracteres invalidos, tente novamente""\n")
    elif (op == "1"):
        email = validar_campo("digite seu email").lower()
        senha = validar_campo("digite sua senha").lower()
        logado = login(email,senha,"1")
        logado2 = login(email,senha,"2")
        if (logado):
            while op == "1":
                menu_adm()
                op1 = input("\nDigite a opção desejada: ").lower()
                if op1 == "10":
                    op = ""
                    logado = False
                funcao_adm(op1, email,senha)
        elif (logado2):
            while op == "1":
                menu_usuarrio()
                op1 = input("\nDigite a opção desejada: ").lower()
                if op1 == "8":
                    logado2 = False
                    op = ""
                fucao_usuario(op1, email,senha,card,cs)
        else:
            print("Email ou senha errado, tente novamente")
            op = ""
    elif (op == "2"):
        registrar = input("\nDigite seu nome para registrar:").lower()
        email = input("Digite seu email:").lower()
        senha = input("Crie uma senha para sua conta:").lower()
        registro(email,senha,registrar,"2")
    elif (op == "3"):
        print("\nVocê esta em modo visitante, não poderá comprar nada, só olhar\n")
        while op == "3":
            menu_visitantes()
            op3 = input("qual opção vc deseja?")
            if op3 == "3":
                op = ""
            funcao_visitantes(op3,dicionario_filmes)
    elif op == "4":
        print('\nO menu foi encerrado.')
        break