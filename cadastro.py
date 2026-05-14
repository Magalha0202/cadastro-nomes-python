nomes = []

# carregar arquivo
try:
    arquivo = open('nomes.txt', 'r')

    for linha in arquivo:
        nome = linha.strip()
        if nome:
            nomes.append(nome)

    arquivo.close()

except FileNotFoundError:
    pass


def salvar_arquivo():
    arquivo = open('nomes.txt', 'w')

    for nome in nomes:
        arquivo.write(nome + '\n')

    arquivo.close()


while True:
    print("\n== SEJA BEM-VINDO ==")
    print('[1] - CADASTRAR NOME')
    print('[2] - LISTAR NOMES')
    print('[3] - REMOVER NOME')
    print('[0] - SAIR')

    try:
        entrada = int(input('ESCOLHA O NÚMERO (0 PARA SAIR): '))
    except ValueError:
        print('Digite apenas números!')
        continue

    if entrada == 0:
        print('Saindo do programa...')
        break

    elif entrada == 1:
        nome = input('Digite o nome completo: ').strip()

        if nome == '':
            print('Você não pode cadastrar um nome vazio!')

        elif nome.lower() in [n.lower() for n in nomes]:
            print('Esse nome já está cadastrado!')

        else:
            nomes.append(nome)
            salvar_arquivo()
            print('Nome cadastrado com sucesso!')

    elif entrada == 2:
        if not nomes:
            print('A lista está vazia!')

        else:
            print('\nLista de nomes:')

            for nome in sorted(nomes, key=str.lower):
                print(nome)

    elif entrada == 3:
        if not nomes:
            print('Não há nomes para remover!')
            continue

        print('\nQual nome deseja remover?')

        for nome in sorted(nomes, key=str.lower):
            print(nome)

        remover = input('Digite o nome completo para remover: ').strip()

        encontrado = False

        for nome in nomes:
            if nome.lower() == remover.lower():
                nomes.remove(nome)
                salvar_arquivo()
                print('Nome removido com sucesso!')
                encontrado = True
                break

        if not encontrado:
            print('Nome não encontrado!')

    else:
        print('Opção inválida!')
