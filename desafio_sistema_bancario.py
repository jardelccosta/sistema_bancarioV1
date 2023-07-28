### Uma string multilinha que representa as opções do menu. 
### O usuário pode selecionar uma dessas opções digitando a letra correspondente.
menu = ''' 

[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair 
 
 => '''

Saldo = 0 #variável numérica para o saldo. Iniciando com R$ 0.00
Limite = 500 # variável que define o limite da conta
Extrato = '' #uma string variz que armazenará as informações das operações
numero_saques = 0 #Variável numérica para controle do saque
LIMITE_SAQUES = 3 #Constante que define o numero máximo de saques permitidos

while True: ## Neste momento entra o código que gera um loop infinito iteragindo com o menu até [q] sair

    opcao = input(menu)
        
        ### Para depositar #####

    if opcao == 'd': ## Se a opção escolhida por a [d]
        # O Código solicitará para que insira o valor 
        valor = float(input('Informe o valor do depósito: ')) 
        #floar converte texto para ponto flutuante. 
        #Input permite que o usuário iserir dados através do teclado durante a execução do programa.


        if valor>0: # Se o valor for maior que zero
            Saldo += valor #vai somar ao saldo atual
            Extrato += f'Depósito: R$ {valor:.2f}\n' #A informação será armazenada na variável extrato
        
        else: # Se o valor for não positivo, vai entrar no bloco else, ou seja, contradiz o if. 
            print("Operação falou! O valor informado é inválido.") #Assim o código irá exibir essa mensagem                          

    elif opcao == 's': # Se a opção escolhida foi Saque.
        #O código solicitará para que insira o valor do saque
        valor = float(input('Informe o valor do saque: ')) # O Usuário irá inserir valor do saque 
        # Input guardará a entrada do usuário;
        # float converte o valor da entrada (que é uma string) para o número decimal (float)

        if valor > Saldo: # Se o valor for maior que o saldo
            print('Operação falhou! Você não tem saldo suficiente.')

        elif valor > Limite: # Se o valor for maior que o limite
            print('Operação falhou! O valor do saque excede o limite disponível.')  

        elif numero_saques >= LIMITE_SAQUES: # Se o numero de saque é maior ou igual ao limite de saque.
            print('Operação falhou! Número máximo de saques excedido.')

        elif valor>0: #Se nenhum dos elif forem atendido e saque for maior que zero.
            Saldo -= valor #Valor do saque é subtraído do saldo atual
            Extrato += f'Saque: R$ {valor:.2f}\n' #A informação do saque é adicionada ao extrato
            numero_saques += 1

        else: #se nenhuma condição if e elif for atendida, o código entra no else. 
            print('Operação falhou! O valor informado é invalido.')

    elif opcao == 'e':
        print('\n========== EXTRATO ==========')
        print('Não foram realizadas movimentações' if not Extrato else Extrato)
        # Aqui o código vai imprir uma expressão condicional. 
        #Verificar se a variável extrato está vazia *not extrato. Se vazio imprime a mensagem "Não forma..."
        #Se Extrato contive alguma informação, imprime as informações do extrato. 
        print(f'\nSaldo: R$ {Saldo:.2f}') # Imprime o saldo atual da conta com duas casas decimais. 
        # A função f-string facilita a formatação de strings interpolando valores e expressões.
        print('================================')

    elif opcao == 'q': 
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")