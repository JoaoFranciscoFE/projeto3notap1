def sudosu (op1):
    while op1 == "sudo su" or op1 == "sudo adm":
        terminal = input("root@cinema:~$").lower()
        if terminal == "quit":
            op1 = ""
        if terminal == "cd /codigo/cinema/":
            while op1 == "sudo su" or op1 == "sudo adm":
                prompt = input("root@cinema:~/codigo/cinema$").lower()
                if prompt == "quit":
                    op1 = ""
                if prompt == "ls":
                    while op1 == "sudo su" or op1 == "sudo adm":
                        print("Adm")
                        print("Usuario")
                        print("Menu")
                        print("Registro")
                        print("Projeto")
                        print("\nA linguagem Utilizada para fazer esse programa é Python 3\n")
                        prompt = input("root@cinema:~/codigo/cinema$").lower()
                        if prompt == "quit":
                            op1 = ""
                        if prompt == "adm":
                            print("\033[31m" + '''from registro_login import registro, remover_filme,adicionar_filmes,verificar_filme,registro_adm,remover_ingresso_filmes
from SuperUser import sudosu
from PIL import Image
import matplotlib.pyplot as plt
def validar_campo(texto):
    digitar = input(texto)
    while len(digitar) == 0:
        digitar = input(texto)
    return digitar
def funcao_adm(op1,email,senha,dicionario):
    if op1 != "1" and op1 != "2" and op1 != "3" and op1 != "4" and op1 != "5" and op1 != "6" and op1 != "7" and op1 != "8" and op1 != "9" and op1 != "10" and op1 != "sudo su" and op1 != "sudo adm":
        print("\ncaracteres invalidos, tente novamente\n")
    elif op1 == "1":
        filmes = open('Filmes.txt', 'r')
        ler = filmes.readlines()
        for i in ler:
            filme = i.split(",")
            print(filme[0])
    elif op1 == "2":
        filme_remover = input("Qual filme vc deseja remover?")
        remover_filme("Filmes.txt", filme_remover)
        remover_ingresso_filmes("ingresso_Filmes.txt",filme_remover)
    elif op1 == "3":
        filme_add = input("digite o nome do filme para adicionar")
        teste = verificar_filme(filme_add)
        if teste:
            print("Esse filme ja existe na lista")
        else:
            sala = input("Para qual sala esse filme vai")
            horario = input("Qual o horario que esse filme passara")
            preco = input("Qual o preço dos ingressos")
            ingresso = input("Qual a quantidade de ingressos")
            adicionar_filmes(filme_add, sala, horario, preco, ingresso)
    elif op1 == "4":
        filme_att = 'Filmes.txt'
        file = open(filme_att, 'r')
        linhas = file.readlines()
        file.close()
        if linhas:
            print("Filmes disponíveis:")
            for i in range(len(linhas)):
                linha = linhas[i]
                filme, sala, horario, ingresso, qtde_ingresso = linha.strip().split(',')
                print(f"Filme: {filme.strip()}")
        filme_para_atualizar = input('Digite o nome do filme para atualizar: ').lower()
        filme_atualizar = open(filme_att, 'r')
        conteudo = filme_atualizar.readlines()
        filme_atualizar.close()
        filme_encontrado = False
        filme_atualizar = open(filme_att, 'w')
        for linha in conteudo:
            if filme_para_atualizar in linha.lower():
                filme_encontrado = True
                sala_nova = input('Nova sala: ')
                horario_novo = input('Novo horário: ')
                novo_valor_ingresso = input('Novo valor do ingresso: ')
                qtde_ingresso_novo = input('Nova quantidade de ingressos: ')
                nova_linha = f'{filme_para_atualizar}, {sala_nova}, {horario_novo}, {novo_valor_ingresso}, {qtde_ingresso_novo}\n'
                filme_atualizar.write(nova_linha)
            else:
                filme_atualizar.write(linha)
        filme_atualizar.close()
        if filme_encontrado:
            print("Filme atualizado com sucesso.")
        else:
            print("O filme não foi encontrado no arquivo.")
    elif op1 == "5":
        sessao_att = 'Filmes.txt'
        sessao_a = open(sessao_att, 'r')
        linhas = sessao_a.readlines()
        sessao_a.close()
        if linhas:
            print("Sessões disponíveis:")
            for i in range(len(linhas)):
                linha = linhas[i]
                filme, sala, horario, valor_ingresso, qtde_ingresso = linha.strip().split(',')
                print(f'{i + 1}. Sessão: {horario.strip()}, Filme: {filme.strip()}, Número da sala: {sala.strip()}')
            opcao = int(input("Digite a sessão do filme que deseja alterar (ou 0 para sair): "))
            if opcao != 0 and 0 < opcao <= len(linhas):
                novo_horario = input('Digite o novo horário: ')
                nova_sala = input('Digite a nova sala: ')
                filme, sala, _, valor_ingresso, qtde_ingresso = linhas[opcao - 1].strip().split(',')
                linhas[opcao - 1] = f'{filme.strip()}, {nova_sala.strip()}, {novo_horario.strip()}, {valor_ingresso.strip()}, {qtde_ingresso.strip()}\n'
                sessao = open(sessao_att, 'w')
                sessao.writelines(linhas)
                sessao_a.close()
                print("Sessão atualizada com sucesso.")
            else:
                print("Opção inválida.")
        else:
            print("Não há sessões disponíveis.")
    elif op1 == "6":
        registrar_adm = input("Digite seu nome para registrar").lower()
        email = input("Digite seu email").lower()
        senha = input("Senha para sua conta").lower()
        registro_adm(email, senha, registrar_adm, "1")
    elif op1 == "7":
        ingresso_att = 'Filmes.txt'

        file = open(ingresso_att, 'r')
        linhas = file.readlines()
        file.close()
        print("Filmes disponíveis:")
        for linha in linhas:
            filme, sala, horario, valor_ingresso, qtde_ingresso = linha.strip().split(',')
            print(f"Filme: {filme.strip()}, Valor do Ingresso: {valor_ingresso.strip()}$, Ingressos disponíveis: {qtde_ingresso.strip()} ")
        alterar_ingresso = input("Gostaria de alterar algum ingresso? (sim/não): ").lower()
        if alterar_ingresso == "sim":
            for i in range(len(linhas)):
                linha = linhas[i]
                filme, sala, horario, ingresso, qtde_ingresso = linha.strip().split(',')
                print(f"{i + 1}. Filme: {filme.strip()}")
            opcao = int(input("Digite o número do filme que você quer alterar o valor e a quantidade de ingressos (ou 0 para sair): ")) - 1
            if 0 <= opcao < len(linhas):
                novo_valor_ingresso = input("Qual o novo valor do ingresso? ").strip()
                nova_quantidade_ingressos = input("Qual a nova quantidade do ingresso? ").strip()
                filme, sala, horario, _, _ = linhas[opcao].strip().split(',')
                linhas[opcao] = f"{filme.strip()}, {sala.strip()}, {horario.strip()}, {novo_valor_ingresso}, {nova_quantidade_ingressos}\n"

                file = open(ingresso_att, 'w')
                file.writelines(linhas)
                file.close()

                print("Valores do ingresso atualizados com sucesso.")
            else:
                print("Filme não encontrado, nenhum ingresso alterado.")
        else:
            print("Nenhum ingresso foi alterado.")
    elif op1 == "8":
        ler_ganhos = 'ingresso_Filmes.txt'

        calc_ganhos = open(ler_ganhos, 'r')
        linhas = calc_ganhos.readlines()

        filmes = []
        ingressos_vendidos = []
        ganhos = []

        for linha in linhas:
            filme, ingresso, ganho = linha.strip().split(':')
            ingresso = int(ingresso)
            ganho = int(ganho)
            filmes.append(filme)
            ingressos_vendidos.append(ingresso)
            ganhos.append(ganho)

        plt.figure(figsize=(10, 6))
        plt.bar(filmes, ganhos, color='skyblue')
        plt.xlabel('Filmes')
        plt.ylabel('Ganhos')
        plt.title('Ganhos por Filme')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('graficos_ganhos.png')

        img = Image.open('graficos_ganhos.png')
        img.show()
        #plt.show()
    elif op1 == '9':
        show_ganhos = open('ingressos_clientes.txt', 'r')
        linhas = show_ganhos.readlines()
        show_ganhos.close()
        ganhos = {}
        for linha in linhas:
            email, valor = linha.strip().split(':')
            valor = float(valor)
            if email in ganhos:
                ganhos[email] += valor
            else:
                ganhos[email] = valor
        emails = list(ganhos.keys())
        valores = list(ganhos.values())
        plt.figure(figsize=(10, 6))
        plt.bar(emails, valores, color='skyblue')
        plt.xlabel('Emails')
        plt.ylabel('Ingressos')
        plt.title('Compras de ingresso por Email')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('graficos_ingressos.png')

        img = Image.open('graficos_ingressos.png')
        img.show()
        #plt.show()''' + "\033[0m")
                        elif prompt == "usuario":
                            print('''from registro_login import *
def fucao_usuario(op1, email, senha, dicionario, dicionario_login, dicionario_ganhos, dicionario_creditos,card,cs):
    if op1 != "1" and op1 != "2" and op1 != "3" and op1 != "4" and op1 != "5" and op1 != "6" and op1 != "7" and op1 != "8":
        print("\ncaracteres invaldos, tente novamente\n")
    elif op1 == "1":
        arq = open('Filmes.txt','r')
        ler = arq.readlines()
        for i in ler:
            conv = i.split(',')
            print(f"\nO filme {conv[0]} está custando {conv[3]}R$")
        comp = input("\ngostaria de comprar ingresso de qual filme?").lower()
        verificar = verificacao_cartao(email,senha,'2',card,cs)
        if verificar:
            comprar = verificar_filme(comp)
            if comprar:
                print("1: Comprar com cartão\n2: Comprar com CScoins\n3: Sair")
                pagar = input("Digite a opção de pagamento:").lower()
                if pagar != "1" and pagar != "2" and pagar != "3":
                    print("caracteres invalidos")
                elif pagar == "1":
                    mostar_ingresso(comp)
                    qtdade = int(input("Quantos ingressos gostaria de comprar?"))
                    converter_ingresso(comp, qtdade)
                    comprar_com_cartao(comp,qtdade,email,senha,"2",card,cs)
                elif pagar == "2":
                    mostar_ingresso(comp)
                    qtdade = int(input("\nQuantos ingressos você gostaria de comprar?"))
                    comprar_com_cscoins(comp,qtdade,email,senha,"2",card,cs)
                elif pagar == "3":
                    print("Você não comprou nenhum ingresso")
                    print("Voltando ao menu...\n")
        else:
            print("\nos ingressos desse filme acabaram ou o filme que gostaria não esta na lista\n")
    elif op1 == "2":
        print("As sessões no momentos são:")
        with open("Filmes.txt","r") as filme:
            ler = filme.readlines()
        for h in ler:
            conv = h.split(",")
            print(f"\nEsta passando {conv[0]} às {conv[2]} na sala {conv[1]} não perca!")
    elif op1 == "3":
        filme = input("Qual filme deseja buscar")
        buscar_filme(filme)
    elif op1 == "4":
        while op1 == "4":
            print("digite o email e senha para registar o cartão\n")
            email = input("Digite seu email:").lower()
            senha = input("Digite sua senha:").lower()
            log_card = log_cartao(email,senha,"2")
            teste = verificacao_cartao(email,senha,"2",card,cs)
            if teste:
                print("Vc ja tem um cartão registrado")
                op1 = ""
            else:
                if log_card:
                    card = input("digite o numero do seu cartão para registrar")
                    registrar_card(email,senha,"2",card,"10")
                    op1 = ""
                else:
                    print("Login ou senha errados")
                    denovo = input("Gostaria de tentar novamente?").lower()
                    if denovo != 'sim':
                        op1 = ""
    elif op1 == "5":
        if verificacao_cartao(email,senha,"2",card,cs):
            print("1: 20$ = 30CScoins\n2: 50$ = 60CScoins\n3: 100$ = 120CScoins\n4: E se vc é Rico ou Rene, 1000$ = PASSE LIVRE\n5: Sair")
            comprar_cscoins(email,senha,"2",card,cs)
    elif op1 == "6":
        atribuir_dados(email,senha,"2",card,cs)
    elif op1 == "7":
        ver_total_ingressos(email)''')
                        elif prompt == "menu":
                            print('''def menu_adm():
    print("---------MENU dos ADM----------\n\n1: Listar filmes\n2: Remover filme\n3: Adicionar filme\n4: Atualizar filme\n5: Gerenciar sessões\n6: Registar ADM\n7: Gerenciar ingressos\n8: Conferir ganhos\n9: Fazer logout")


def menu_usuarrio():
    print("---------MENU dos USUARIOS----------\n")
    print('1: Comprar ingresso\n2: Ver sessões\n3: Cadastrar cartão\n4: Comprar CScoins\n5: Seus dados\n6: Logout')

def menu_visitantes():
    print('---------MENU dos VISITANTES----------\n')
    print("1: Ver filmes e sessões\n2: Ajuda\n3: Sair")


def funcao_visitantes(op3, dicionario):
    if op3 != "1" and op3 != "2" and op3 != "3":
        print("\nCaractéres invalidos, tente novamente\n")
    elif op3 == "1":
        print('---------FILMES----------\n')
        for sessao in dicionario:
            print(f'Está passando {sessao} às {dicionario[sessao][1]} na sala {dicionario[sessao][0]} e esta custando {dicionario[sessao][2]}R$\n')
    elif op3 == "2":
        print(''''''1-Como comprar ingressos? você precisará primeiramente se registrar
e registar seu cartão, para poder ter o acesso a area de comprar\n
2-Como se Registrar? va no MENU inicial e aperte 2 para realizar o seu registro
depois que você fizer o registro, aperte 1 no MENU inical para efetuar login\n
3-Como Registro meu cartão? no MENU de usuario aperte 3 para realizar o registro do seu cartão
logo em seguida preencha conforme pede e coloque o numero do cartão para registrar\n
4-Oque é CScoins? CScoins ou "Computer Science coins" é a moeda utilizada no nosso
registro_login no sistema de compras de ingressos, ela traz discontos para o comprador
em compra de ingressos e futuramente para mais serviços do nosso Cinema!\n
5-Em mais duvidas consultar os ADM @Guilherme Soares @João Francisco e se não conseguiram te ajudar
consultar o brabo dos brabo @Rene.Gadelha Casca de bala Oficial!\n''''')
                elif prompt == "registro":
                    print('''import os
from random import randint

# Usado em registro para verificar se ja ah esse email registrado
def verificacao(email):
    arq = open("login_geral.txt", "r")
    ler = arq.readlines()
    for user in ler:
        verificar = user.strip().split(":")
        if verificar[0] == email:
            return True
    arq.close()
    return False
# Usado na parte para registrar o cartão
def log_cartao(email, senha, tipo):
    arq = open("login_geral.txt", "r")
    ler = arq.readlines()
    for user in ler:
        verificar = user.strip().split(":")
        if verificar[0] == email and verificar[1] == senha and verificar[2] == tipo:
            return True
    arq.close()
    return False
# Usado para verificar se o cartão ja esta registrado
def verificacao_cartao(email, senha, tipo, card, cs):
    arq = open("cartao_credito.txt", "r")
    ler = arq.readlines()
    for user in ler:
        verificar = user.strip().split(":")
        card = verificar[3]
        cs = verificar[4]
        if verificar[0] == email and verificar[1] == senha and verificar[2] == tipo and verificar[3] == card and \
                verificar[4] == cs:
            return True
    arq.close()
    return False
# Usado para fazer o registro de um usuario
def registro(email, senha, nome, tipo):
    if verificacao(email):
        print("Email ja existe, tente novamente")
    else:
        with open("login_geral.txt", "a") as arq, open("ingressos_clientes.txt","a") as file:
            arq.write("\n" + email + ":" + senha + ":" + tipo + ":" + nome)
            file.write(email + ":" + "0" + "\n")
def registro_adm(email, senha, nome, tipo):
    if verificacao(email):
        print("Email ja existe, tente novamente")
    else:
        arq = open("login_geral.txt", "a")
        arq.write("\n" + email + ":" + senha + ":" + tipo + ":" + nome)
        arq.close()
# Usado para fazer o login dos usuarios e adm
def login(email, senha, tipo):
    arq = open("login_geral.txt", "r")
    users = arq.readlines()
    saida = False
    for user in users:
        log_email, log_senha, log_tipo, nome = user.split(':')
        log_email = log_email.replace("\n", "")
        if log_email == email and log_senha == senha and log_tipo == tipo:
            print(f"\nBem vindo {nome}\n")
            saida = True
            break
    arq.close()
    return saida
def login_card(email, senha, tipo):
    arq = open("login_geral.txt", "r")
    users = arq.readlines()
    saida = False
    for user in users:
        log_email, log_senha, log_tipo, nome = user.split(':')
        log_email = log_email.replace("\n", "")
        if log_email == email and log_senha == senha and log_tipo == tipo:
            saida = True
            break
    arq.close()
    return saida
# Usado pra registrar o cartão
def registrar_card(email, senha, tipo, card, cs):
    if verificacao_cartao(email, senha, tipo, card, cs):
        print("esse cartão ja esta registrado")
    else:
        arq = open('cartao_credito.txt', "a")
        arq.write(email + ":" + senha + ":" + tipo + ":" + card + ":" + cs + "\n")
        arq.close()
# Usado para mostrar os dados do usuario
def atribuir_dados(email, senha, tipo, card, cs):
    if login_card(email, senha, tipo):
        aqr = open("login_geral.txt", "r")
        ler = aqr.readlines()
        for i in ler:
            dados_email, dados_senha, dados_tipo, nome = i.split(":")
            if dados_email == email and dados_senha == senha and dados_tipo == tipo:
                print(f"\nSeu Email {dados_email}")
                print(f"Sua senha {dados_senha}")
                print(f"Seu nome {nome}")
        aqr.close()
    if verificacao_cartao(email, senha, tipo, card, cs):
        arq1 = open('cartao_credito.txt', 'r')
        ler1 = arq1.readlines()
        for o in ler1:
            conve = o.split(":")
            card = conve[3]
            cs = conve[4]
            if conve[0] == email and conve[1] == senha and conve[2] == tipo and conve[3] == card and conve[4] == cs:
                print(f"Seu cartão: {conve[3]}")
                print(f"Suas CSCoins: {conve[4]}")
        arq1.close()
    else:
        print("Vc ainda não tem cartão registrado")
def converter_cscoins(email, senha, tipo, card, cs):
    arq = open('cartao_credito.txt', "r")
    ler = arq.readlines()
    for i in ler:
        conv = i.strip().split(":")
        if verificacao_cartao(email, senha, "2", card, cs):
            cs = int(conv[4])
            aqr = open('Filmes.txt', 'r')
def converter_ingresso(comprar, quantidade):
    with open('Filmes.txt', 'r') as file:
        linhas = file.readlines()
    for i in range(len(linhas)):
        linha = linhas[i]
        elementos = linha.split(',')
        if elementos[0] == comprar:
            numero = int(elementos[4])
            if quantidade > numero or quantidade <= 0:
                print("O valor não corresponde a quantidade")
                break
            novo_numero = numero - quantidade
            elementos[4] = str(novo_numero)
            linhas[i] = ','.join(elementos) + '\n'
    with open('Filmes.txt', 'w') as file:
        file.writelines(linhas)
def mostar_ingresso(comprar):
    with open('Filmes.txt', 'r') as file:
        ler = file.readlines()
        for i in ler:
            conv = i.split(',')
            if conv[0] == comprar:
                print("")
                print(f"Esse filme tem {conv[4].replace('\n', '')} ingressos")


def verificar_filme(comp):
    arq = open('Filmes.txt', 'r')
    ler = arq.readlines()
    for i in ler:
        conve = i.split(',')
        if conve[0] == comp:
            return True
    print("\nesse filme não esta na lista\n")
    return False
def comprar_com_cartao(comp,quantidade, email, senha, tipo, card, cs):
    preco = 0
    with open("Filmes.txt","r") as file:
        ler = file.readlines()
    for i in ler:
        conv = i.split(",")
        if conv[0] == comp:
            preco = int(conv[3])
    with open("cartao_credito.txt", 'r') as file2:
        ler2 = file2.readlines()
    for o in range(len(ler2)):
        conv = ler2[o]
        elementos2 = conv.split(':')
        if verificacao_cartao(email,senha,"2", card,cs):
            if elementos2[0] == email and elementos2[1] == senha:
                with open("nota_fiscal.txt", "a") as nota:
                    nota.write(f"________Nota_Fiscal________\n"
                               f"Numero fiscal:  {randint(1, 1000000)}\n"
                               f"\n"
                               f"{email}: {quantidade} ingressos\n"
                               f"\n"
                               f"Filme {comp}\n"
                               f"\n"
                               f"Comprovante de compra.\n"
                               f"\n"
                               f"Obg pela preferencia! :)\n"
                               f"___________________________\n")
                converter_ingresso_txt(comp,quantidade,email,senha,"2",card,cs)
                converter_ingresso_usuario_txt(quantidade,email,senha,"2",card,cs)
                converter_ganhos_txt(preco,comp,quantidade,email,senha,"2",card,cs)
                csc = int(elementos2[4])
                novo = csc + 5 * quantidade
                elementos2[4] = str(novo)
                ler2[o] = ':'.join(elementos2) + '\n'
    with open("cartao_credito.txt", 'w') as file2:
        file2.writelines(ler2)
def comprar_com_cscoins(comprar, quantidade, email, senha, tipo, card, cs):
    preco = 0
    with open("Filmes.txt", 'r') as file1:
        ler1 = file1.readlines()
    with open("cartao_credito.txt", 'r') as file2:
        ler2 = file2.readlines()
    for i in range(len(ler1)):
        linha1 = ler1[i]
        elementos1 = linha1.strip().split(',')
        if elementos1[0] == comprar:
            preco = int(elementos1[3])
            break
    for o in range(len(ler2)):
        conv = ler2[o]
        elementos2 = conv.strip().split(':')
        if verificacao_cartao(email, senha, "2", card, cs):
            if elementos2[0] == email and elementos2[1] == senha:
                csc = int(elementos2[4])
                if preco * quantidade > csc:
                    print("Vc não tem CScoins suficiente")
                    break
                with open("nota_fiscal.txt", "a") as nota:
                    nota.write(f"________Nota_Fiscal________\n"
                               f"Numero fiscal:  {randint(1, 1000000)}\n"
                               f"\n"
                               f"{email}: {quantidade} ingressos\n"
                               f"\n"
                               f"Filme {comprar}\n"
                               f"\n"
                               f"Comprovante de compra.\n"
                               f"\n"
                               f"Obg pela preferencia! :)\n"
                               f"___________________________\n")
                converter_ingresso_usuario_txt(quantidade,email,senha,"2",card,cs)
                converter_ingresso_txt(comprar,quantidade,email,senha,"2",card,cs)
                converter_ganhos_txt(preco,comprar,quantidade,email,senha,"2",card,cs)
                converter_ingresso(comprar, quantidade)
                csc -= preco * quantidade
                novo = csc
                elementos2[4] = str(novo)
                ler2[o] = ':'.join(elementos2) + '\n'
    with open("cartao_credito.txt", 'w') as file2:
        file2.writelines(ler2)
def comprar_cscoins(email, senha, tipo, card, cs):
    with open("cartao_credito.txt", 'r') as file2:
        ler2 = file2.readlines()
    for o in range(len(ler2)):
        conv = ler2[o]
        elementos2 = conv.strip().split(':')
        if verificacao_cartao(email, senha, "2", card, cs):
            if elementos2[0] == email and elementos2[1] == senha:
                csc = int(elementos2[4])
                cscoins = input("Qual opção acima gostaria de comprar?").lower()
                if cscoins == "1":
                    csc += 30
                    novo = csc
                    elementos2[4] = str(novo)
                    ler2[o] = ':'.join(elementos2) + '\n'
                    break
                elif cscoins == "2":
                    csc += 60
                    novo = csc
                    elementos2[4] = str(novo)
                    ler2[o] = ':'.join(elementos2) + '\n'
                    break
                elif cscoins == "3":
                    csc += 120
                    novo = csc
                    elementos2[4] = str(novo)
                    ler2[o] = ':'.join(elementos2) + '\n'
                    break
                elif cscoins == "4":
                    csc += 1000
                    novo = csc
                    elementos2[4] = str(novo)
                    ler2[o] = ':'.join(elementos2) + '\n'
                    break
                elif cscoins == "5":
                    print("nenhuma CScoins foi adicionada")
                    break
                else:
                    print("caracteres invalidos")
    with open("cartao_credito.txt", 'w') as file2:
        file2.writelines(ler2)
# PARTE DOS ADM
def remover_filme(nome_arquivo, remover):
    nome_arquivo_temp = 'temp_' + "Filmes.txt"
    with open("Filmes.txt", 'r') as file_in, open(nome_arquivo_temp, 'w') as file_out:
        for linha in file_in:
            linha = linha.strip()
            elementos = linha.split(',')
            if elementos[0] != remover:
                file_out.write(linha + '\n')
    os.remove("Filmes.txt")
    os.rename(nome_arquivo_temp, "Filmes.txt")

def remover_ingresso_filmes(nome_arquivo, remover):
    nome_arquivo_temp = 'temp_' + "ingresso_Filmes.txt"
    with open("ingresso_Filmes.txt", 'r') as file_in, open(nome_arquivo_temp, 'w') as file_out:
        for linha in file_in:
            linha = linha.strip()
            elementos = linha.split(':')
            if elementos[0] != remover:
                file_out.write(linha + '\n')
    os.remove("ingresso_Filmes.txt")
    os.rename(nome_arquivo_temp, "ingresso_Filmes.txt")

def adicionar_filmes(filme_adicionar, sala, horario, preco, ingresso):
    if verificar_filme(filme_adicionar):
        return False
    else:
        with open("Filmes.txt", "a") as add, open("ingresso_Filmes.txt","a") as file:
            add.write(filme_adicionar + "," + sala + "," + horario + "," + preco + "," + ingresso + "\n")
            file.write(filme_adicionar + ":" + "0" + ":" + "0" + "\n")

def remover_historico(nome_arquivo, remover):
    nome_arquivo_temp = 'temp_' + "ingresso_Filmes.txt"
    with open("ingresso_Filmes.txt", 'r') as file_in, open(nome_arquivo_temp, 'w') as file_out:
        for linha in file_in:
            linha = linha.strip()
            elementos = linha.split(':')
            if elementos[0] != remover:
                file_out.write(linha + '\n')
    os.remove("ingresso_Filmes.txt")
    os.rename(nome_arquivo_temp, "ingresso_Filmes.txt")

def verificar_filme(filme_adicionar):
    with open("Filmes.txt", "r") as filme:
        ler = filme.readlines()
    for i in ler:
        conv = i.split(",")
        if conv[0] == filme_adicionar:
            return True
    return False

def buscar_filme(buscar):
    with open("Filmes.txt","r") as filme:
        ler = filme.readlines()
    for i in ler:
        conv = i.split(",")
        if conv[0] == buscar:
            print("Filme encontrado")
            print(f"{conv[0]}, esta cusanto ${conv[3]} e esta passando as {conv[2]}")
            break
        else:
            print("Filme não encontrado :( ")
            break

def hitorico_ingresso():
    with open("nota_fiscal.txt","r") as nota:
        ler = nota.readlines()
    print("Todos ingressos comprados")
    for i in ler:
        conv = i.split(",")
        print(f"{conv[0]} e {conv[1]}")


def converter_ingresso_txt(comp,quantidade, email, senha, tipo, card, cs):
    with open("ingresso_Filmes.txt", 'r') as file2:
        ler2 = file2.readlines()
    for o in range(len(ler2)):
        conv = ler2[o]
        elementos2 = conv.split(':')
        if verificacao_cartao(email, senha, "2", card, cs):
            if elementos2[0] == comp:
                conv = int(elementos2[1])
                novo = conv + quantidade
                elementos2[1] = str(novo)
                ler2[o] = ":".join(elementos2)
    with open("ingresso_Filmes.txt", 'w') as file2:
        file2.writelines(ler2)

def converter_ingresso_usuario_txt(quantidade, email, senha, tipo, card, cs):
    with open("ingressos_clientes.txt", 'r') as file2:
        ler2 = file2.readlines()
    for o in range(len(ler2)):
        conv = ler2[o]
        elementos2 = conv.split(':')
        if verificacao_cartao(email, senha, "2", card, cs):
            if elementos2[0] == email:
                conv = int(elementos2[1])
                novo = conv + quantidade
                elementos2[1] = str(novo)
                ler2[o] = ":".join(elementos2) + "\n"
    with open("ingressos_clientes.txt", 'w') as file2:
        file2.writelines(ler2)

def converter_ganhos_txt(preco,comp,quantidade, email, senha, tipo, card, cs):
    with open("ingresso_Filmes.txt", 'r') as file2:
        ler2 = file2.readlines()
    for o in range(len(ler2)):
        conv = ler2[o]
        elementos2 = conv.split(':')
        if verificacao_cartao(email, senha, "2", card, cs):
            if elementos2[0] == comp:
                conv = int(elementos2[2])
                novo = conv + (quantidade * preco)
                elementos2[2] = str(novo)
                ler2[o] = ":".join(elementos2) + "\n"
    with open("ingresso_Filmes.txt", 'w') as file2:
        file2.writelines(ler2)

def ver_total_ingressos(email):
    with open("ingressos_clientes.txt" , 'r') as file:
        ler = file.readlines()
    for i in ler:
        conv = i.split(":")
        if conv[0] == email:
            print("Total de ingressos comprados")
            print(f"{email}: {conv[1].replace('\n','')} ingressos")
            break''')