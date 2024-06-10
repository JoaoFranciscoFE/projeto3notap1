import os
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
            break
    '''ingressos = {}

    file = open('ingressos_clientes.txt', 'r')
    linhas = file.readlines()
    file.close()

    for linha in linhas:
        email, qtd = linha.strip().split(':')
        ingressos[email] = int(qtd)

    print("Ingressos comprados:")
    for email, qtd in ingressos.items():
        print(f"{email}: {qtd} ingressos")'''