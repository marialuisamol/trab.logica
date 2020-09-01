#ALUNOS: Fernando Mertinho, RA:
# Maria Luísa Mendonça RA: 0049545


alfabeto = ['P', 'Q', 'R', '(', ')', '~', '$', 'v', '^', '>']
letras = ['P', 'Q', 'R']
operadores = ['$', 'v', '^', '>']
dif = ['~','(',')']

i = 0
op = 0


def check_position():
      for position, item in enumerate(formula):
            if item == 'v':
                if position == 0:
                    print('Fórmula inválida!, você inseriu um argumento inválido na primeira posição da formula, tente novamente')
                    break
            if item == '^':
                if position == 0:
                    print('Fórmula inválida!, você inseriu um argumento inválido na primeira posição da formula, tente novamente')
                    break
            if item == '>':
                if position == 0:
                    print('Fórmula inválida!, você inseriu um argumento inválido na primeira posição da formula, tente novamente')
                    break
            if item == '$':
                if position == 0:
                    print('Fórmula inválida!, você inseriu um argumento inválido na primeira posição da formula, tente novamente')
                    break
            else:
                check_operadores()
                break


def check_operadores():
    verif = 0
    for i in range(len(formula)-1):
        if formula[i] in operadores:
            if formula[i + 1] in letras or formula[i + 1] in dif:
                formula[i + 1]
                verif += 1

            else:
                print('Inválida. Tente novamente!')
                break

        elif formula[i] in letras:
            if formula[i + 1] in operadores or formula[i + 1] in dif:
                formula[i + 1]
                verif += 1
            else:
                print('Fórmula inválida! Tente novamente!')
                break

        elif formula[i] in dif:
            if formula[i] != formula[i+1] or formula[i] != operadores:
                verif += 1
            else:
                print('Fórmula inválida! Tente novamente!')
                break

    if verif == len(formula)-1:
        print('Fórmula Válida!')



def check_alfabeto():
    if set(formula).intersection(alfabeto):
            check_position()
    else:
        print('Fórmula inválida!')

while op != 4:
    print('\n\nMENU DE OPERAÇÕES: \n'
          '1- Informe a fórmula para realizar as operações; \n'
          '2- Verifica se a fórmula é válida; \n'
          '3- Calcular o tamanho da fórmula.\n'
          '4- Fecha o programa\n')

    op = int(input('Digite a operação desejada: '))

    if op == 1:

        print('REGRAS: \n'
              'O alfabeto usado será: P, Q e R; \n'
              'Os simbolos proposicionais são:\nNegação = ~\nOu,Or = v\nSe somente se = $\nAnd, Conjução = ^\nSe,Implicação = >\n'
              'Pode-se usar apenas uma vez cada símbolo de pontuação;\n'
              'O tamanho máximo de cada fórmula é de 12 caracteres (considerando também os símbolos).')

        formula = input('Digite a fórmula: ')

        if len(formula) > 12:
            print('Fórmula inválida!')

        else:
            print('\nA fórmula digitada é: ', formula)

    if op == 2:
        formula
        check_alfabeto()




    #função len calcula o tamanho da formula contando todos os caracteres incluindo ()
    if op == 3:
        print('Tamanho da fórmula é: ', len(formula))
