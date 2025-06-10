menu = """

Seja bem-vindo(a) ao Sistema Bancário!

Escolha a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato_deposito = ""
extrato_saque = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        while True:

            valor_deposito = float(
                input("\nInsira o valor a ser depositado: "))

            if valor_deposito > 0:

                print('\nDepósito realizado!')
                saldo += valor_deposito
                print(f'\nValor depositado: {valor_deposito}')
                print(f'Saldo disponível: {saldo}')
                extrato_deposito += f"Depósito: R$ {valor_deposito:.2f}\n"

                print(
                    '\nDesejar realizar um novo depósito?\n\n[s]: sim\n[n]: não')

                decisao = input('\n=> ')

                if decisao == 's':
                    continue

                elif decisao == 'n':
                    break

                else:
                    print('Operação Inválida! Escolha uma das opções acima.')

            else:
                print("Operação inválida! Insira um valor válido.")

    elif opcao == "2":

        while True:

            valor_saque = float(input("\nInsira o valor a ser sacado: "))

            if valor_saque <= saldo:

                if numero_saques < LIMITE_SAQUES:

                    if valor_saque > 0:

                        if valor_saque <= limite:
                            print('Saque realizado!')
                            numero_saques += 1
                            print(f'N° saques: {numero_saques}')
                            saldo -= valor_saque
                            print(f'Saldo disponível: {saldo}')
                            extrato_saque += f"Saque: R$ {valor_saque:.2f}\n"

                        else:
                            print(
                                'Limite excedido! Insira um valor dentro do limite.')

                        print(
                            '\nDesejar realizar um novo saque?\n\n[s]: sim\n[n]: não')

                        decisao = input('\n=> ')

                        if decisao == 's':
                            continue

                        elif decisao == 'n':
                            break

                        else:
                            print('Operação Inválida! Escolha uma das opções acima.')

                    else:
                        print("Operação inválida! Insira um valor válido.")

                else:
                    print(
                        'Limite de saque diários excedido! Tente novamente no dia seguinte.')
                    break

            else:
                print('Operação inválida! Saldo insuficiente.')
                break

    elif opcao == "3":

        while True:

            print("\nExtrato de Movimentações")

            if extrato_deposito or (extrato_saque and extrato_deposito):
                print('\n• Depósitos realizados:')
                print(f'\n{extrato_deposito}')

            if extrato_saque or (extrato_saque and extrato_deposito):
                print('\n• Saques realizados:')
                print(f'\n{extrato_saque}')

            print(f'\nSaldo atual: {saldo}')

            if not (extrato_saque or extrato_deposito or (extrato_saque and extrato_deposito)):
                print('\nNão foram realizadas movimentações.')

            print('\nDesejar sair?\n\n[s]: sim\n[n]: não')

            decisao = input('\n=> ')

            if decisao == 's':
                break

            elif decisao == 'n':
                continue

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")