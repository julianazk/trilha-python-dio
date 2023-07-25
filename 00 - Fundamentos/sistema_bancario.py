menu='''
########### Bem vindo ao banco ###########
Menu:
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
numero_saque = 0
valor_deposito = 0
extrato = ""
LIMITE_SAQUES = 3

while True:
    operacao = input(menu)

    if operacao == 's':
        if numero_saque < 3:
            valor_saque = input('Digite o valor: ')
            if float(valor_saque) > 0:
                if float(valor_saque) <= float(limite):
                    if float(valor_saque) <= float(saldo):
                        saldo = float(saldo) - float(valor_saque)
                        numero_saque += 1
                        extrato = extrato + 'Saque: ' + valor_saque + '\n'
                    else:
                        print('Saldo insuficiente')
                else:
                    print('Limite excedido')
            else:
                print('Valor inválido')
        else:
            print('Limite de saques atingido')
    elif operacao == 'd':
        valor_deposito = input('Digite o valor: ')
        if valor_deposito > 0:
            saldo = saldo + float(valor_deposito)
            extrato = extrato + 'Deposito: ' + valor_deposito + '\n'
        else:
            print('Valor inválido')
    elif operacao == 'e':
        print('==========EXTRATO==========')
        if extrato == "":
            print('Sem movimentações')
        else:
            print(extrato)
        print('Saldo: ' + str(saldo))
        print('Quantidade de saques: ' + str(numero_saque))
        print('===========================')
    elif operacao == 'q':
        break

print('Obrigado por utilizar nossos serviços')



