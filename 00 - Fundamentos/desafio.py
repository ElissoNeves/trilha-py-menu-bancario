menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """
# menu modificado: as opções foram trocadas de letras(d, s, e, q) para (1, 2, 3 e 4)
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")
        # Texto modificado
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        # Texto modificado
        elif excedeu_limite:
            print("O valor do saque excede o limite.")
        # Texto modificado
        elif excedeu_saques:
            print("Número máximo de saques excedido.")
        # Texto modificado
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso. ")

        else:
            print("O valor informado é inválido.")
        # Texto modificado
    elif opcao == "3":
        print("\n_______________ EXTRATO _________________")
        print("Voçê está sem saldo, realize um depósito." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("_________________________________________")
        # Print do Extrato modificado
    elif opcao == "4":
        print("Saindo... ")
        break
        # print adicionado: print("Saindo... ")
    else:
        print("Opção incorreta, por favor selecione novamente a operação desejada.")
        # Texto modificado