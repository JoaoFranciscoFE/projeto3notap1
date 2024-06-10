
def menu_adm():
    print("---------MENU dos ADM----------\n\n1: Listar filmes\n2: Remover filme\n3: Adicionar filme\n4: Atualizar filme\n5: Gerenciar sessões\n6: Registar ADM\n7: Gerenciar ingressos\n8: Conferir ganhos\n9: Conferir compra de usuarios especificos\n10: Fazer logout")


def menu_usuarrio():
    print("---------MENU dos USUARIOS----------\n")
    print('1: Comprar ingresso\n2: Ver sessões\n3: Buscar Filme\n4: Cadastrar Cartão\n5: Comprar CSCoins\n6: Seus dados\n7: Ver total de ingressos\n8: Logout')

def menu_visitantes():
    print('---------MENU dos VISITANTES----------\n')
    print("1: Ver filmes e sessões\n2: Ajuda\n3: Sair")


def funcao_visitantes(op3, dicionario):
    if op3 != "1" and op3 != "2" and op3 != "3":
        print("\nCaractéres invalidos, tente novamente\n")
    elif op3 == "1":
        print('---------FILMES----------')
        with open("Filmes.txt","r") as file:
            ler = file.readlines()
        for i in ler:
            conv = i.strip().split(',')
            print(f"O Filme {conv[0]} está passando as {conv[2]} na sala {conv[1]}, não perca!\n")
    elif op3 == "2":
        print('''1-Como comprar ingressos? você precisará primeiramente se registrar
e registar seu cartão, para poder ter o acesso a area de comprar\n
2-Como se Registrar? va no MENU inicial e aperte 2 para realizar o seu registro
depois que você fizer o registro, aperte 1 no MENU inical para efetuar login\n
3-Como Registro meu cartão? no MENU de usuario aperte 3 para realizar o registro do seu cartão
logo em seguida preencha conforme pede e coloque o numero do cartão para registrar\n
4-Oque é CScoins? CScoins ou "Computer Science coins" é a moeda utilizada no nosso
registro_login no sistema de compras de ingressos, ela traz discontos para o comprador
em compra de ingressos e futuramente para mais serviços do nosso Cinema!\n
5-Em mais duvidas consultar os ADM @Guilherme Soares @João Francisco e se não conseguiram te ajudar
consultar o brabo dos brabo @Rene.Gadelha Casca de bala Oficial!\n''')
