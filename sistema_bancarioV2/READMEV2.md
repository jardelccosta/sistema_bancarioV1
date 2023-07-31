DEIXANDO O CÓDIGO MAIS MODULARIZADO 

  Criar funções para as operações existentes: 
    - Sacar;
          A função saque deve receber argumentos por nome (keyword only)
    - Depositar; e
          Deve receber apenas argumentos por posição (positional only)
    - Extrado.
          Deve receber posição e por nome (positional only and keyword only)
            

Além disso, criar duas novas funções
    - usuário (cliente do banco); e
        Usuário deve ser armazenado em uma lista. É composto por: Nome, data de nascimento, CPF e endereço. O endereço é um string (logradouro, nro - bairro - cidade/sigla estado.)
        Deve ser armazeado somente os numeros do CPF. Não podendo ter2 usuários com o mesmo CPF
    - conta corrente (vincular com o usuário).
        Conta deve ser armazenado em uma lista. Composta por agência, número da conta e usuário. 
        O número da conta é sequêncial, iniciando em 1. 
        O número da agência é fixo: "0001"
        O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário. 
    
    
