from registro_login import registro, remover_filme,adicionar_filmes,verificar_filme,registro_adm,remover_ingresso_filmes
from SuperUser import sudosu
from PIL import Image
import matplotlib.pyplot as plt
def validar_campo(texto):
    digitar = input(texto)
    while len(digitar) == 0:
        digitar = input(texto)
    return digitar
def funcao_adm(op1,email,senha):
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
        #plt.show()
    elif op1 == "sudo su" or op1 == "sudo adm":
        sudosu(op1)