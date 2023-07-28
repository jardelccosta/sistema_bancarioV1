# Resolvendo o problema com ajuda do ChatGPT 

#Iniciando as variáveis 

saldo_atual = 0
limite_saque_diario = 3
limite_saque_valor = 500.00
extrato = []

# A função para realizar um depósito

def depositar(valor): #função que permite realizar deposito na conta
    global saldo_atual # global para indicar que queremos modificar a variavel global "saldo_atual"
    saldo_atual += valor #incrementa o  valor depositado ao saldo atual
    extrato.append('Depósito: + R$ {:.2f}'. format(valor)) #Descrição da movimentação ao extrato atual
    # função append para adicionar essa informação à lista. 

# A função parta realizar saque 
def sacar(valor):
    global saldo_atual, limite_saque_diario
    if valor <= saldo_atual and limite_saque_diario > 0 and valor <= limite_saque_valor:
       saldo_atual -= valor 
       limite_saque_diario -= 1
       extrato.append("Saque: - R$ {:.2f}". format(valor)) 

    elif valor>limite_saque_valor:
        print('Limite de saque diário excedido. O valor máximo permitido é de R$ {:.2f}'.format(limite_saque_valor)) 
    elif valor>saldo_atual:
        print('Saldo insuficiente para realizar o saque. O seu saldo atual é de R$ {:.2f}'.format(saldo_atual))      
    else:
        print('Limite de saques diários atindigo. Você já realizou 3 saques hoje.')              

# Função para exibir o extrato 

def visualizar_extrato():
    global saldo_atual
    if len(extrato) == 0: ## verifica se a lista extrato está vazia
        print('Não foram realizadas movimentações.')
    else:
        for movimento in extrato:
            print(movimento)
    print('Saldo atual: R$ {:.2f}'.format(saldo_atual))  

def formatar_valor (valor): ## Essa função formata um valor numério para o formato R$ xxx.xx
    return "{:.2f}.format(valor)"

## Criando o loop principal 
while True:
    print('\n ---- MENU ----')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Visulizar Extrato')
    print('4. Sair')

    opcao = input('Escolha uma opção (1/2/3/4): ') 

    if opcao == '1':
        valor_deposito = float(input('Digite o valor a ser depositado: '))
        depositar(valor_deposito)
    elif opcao == '2':
        valor_saque = float(input('Digite o valor a ser sacado: '))
        sacar(valor_saque)

    elif opcao == '3':
        visualizar_extrato()

    elif opcao == '4':
        print('Saindo do sistema bancário.')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida')             





