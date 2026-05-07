print('---AGENDA---\n')

agenda = {}

while True:
    entrada = input('\nEscolha um número:\n1. Adicionar\n2. Buscar\n3. Listar\n4. Sair\n')
    if entrada == '1':
        nome_novo = input(f'Digite o nome: ').lower().strip()
        if agenda.get(nome_novo):
            substituir = input(f'{nome_novo} já está salvo em seus contatos.\nDeseja substituir?(S/N): ').lower().strip()
            while substituir not in ('n', 's'):
                print(f'desculpa, não identificamos a opção {substituir}!')
                substituir = input(f'{nome_novo} já está salvo em seus contatos.\nDeseja substituir?(S/N): ').lower().strip()
            if substituir == 'n':
                continue

        telefone_novo = input(f'Digite o telefone: ')
        email_novo = input(f'Digite o email: ')
        contato_novo = {
        'telefone': telefone_novo,
        'email': email_novo
        }
        agenda[nome_novo] = contato_novo

    elif entrada == '2':
        buscar = input(f'Digite o contato: ').lower().strip()
        if buscar in agenda:
            print(f'\nTelefone: {agenda[buscar]["telefone"]}\nEmail: {agenda[buscar]["email"]}')
        else:
            adicionar_inexist = input(f'você deseja adicionar o contato {buscar}? (S/N): ').lower().strip()
            while adicionar_inexist not in ('s', 'n'):
                print(f'desculpa, não identificamos a opção {adicionar_inexist}!')
                adicionar_inexist = input(f'você deseja adicionar o contato {buscar}? (S/N): ').lower().strip()
            if adicionar_inexist == 'n':
                continue
            if adicionar_inexist == 's':
                telefone_novo = input(f'Digite o telefone: ')
                email_novo = input(f'Digite o email: ')
                contato_novo = {
                'telefone': telefone_novo,
                'email': email_novo
                }
                agenda[buscar] = contato_novo

    elif entrada == '3':
        if len(agenda) == 0:
            print('sua agenda está vazia!')
        else:
           for nome, contato in agenda.items():
               print(f'{nome} -> {contato["telefone"]} | {contato["email"]}')

    elif entrada == '4':
        print('você fechou a agenda')
        break

    else:
        print(f'desculpa, não identificamos a opção "{entrada}"\n')


