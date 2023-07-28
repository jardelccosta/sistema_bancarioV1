menu = '''

[d] Depositar 
[s] Scar 
[e] Extrato
[q] Sair 
 
 => '''

Saldo = 0
Limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd': 
        print('Depósito')

    elif opcao == 's': 
        print('Saque')

    elif opcao == 'e':
        print('Extrato')

    elif opcao == 'q': 
        print('Sair') 

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")