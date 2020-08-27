op = 0
while op != 4:
    print('MENU DE OPERAÇÕES: \n'
               '1- Informe a fórmula para realizar as operações; \n'
               '2- Verifica se a fórmula é válida; \n'
               '3- Calcular o tamanho da fórmula.\n'
               '4- Fecha o programa\n')

    op = int(input('Digite a operação desejada: '))


    if op == 1:

        print('REGRAS: \n'
              'O alfabeto usado será: P, Q e R; \n'
              'Pode-se usar apenas uma vez cada símbolo de pontuação;\n'
              'Os operadores deverão ser informados da seguinte maneira: \n'
              ' Negação ~\n Conjunção '
              'O tamanho máximo de cada fórmula é de 12 caracteres (considerando também os símbolos).')

        formula = input('Digite a fórmula: ')

        if len(formula) > 12:
            print('Fórmula inválida!')

        else:
            print('\nA fórmula digitada é: ', formula)


    if op == 2:
        for cont in formula:
            

    if op == 3:
        print('Tamanho da fórmula é: ', len(formula))