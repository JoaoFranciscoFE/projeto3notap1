from registro_login import *
def fucao_usuario(op1, email, senha,card,cs):
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
        ver_total_ingressos(email)