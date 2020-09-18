#ALUNOS: Fernando Mertinho, RA: 0040886
# Maria Luísa Mendonça RA: 0049545

import ttg

alfabeto = ['P', 'Q', 'R', '(', ')', '~', '$', 'v', '^', '>']
letras = ['P', 'Q', 'R']
operadores = ['$', 'v', '^', '>']
sim = ['(', ')']

i = 0
op = 1


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
                check_sintaxe()
                break

def check_operando():
    for i in range(len(formula)-1):
        if formula[i] in operando:
            if formula[i + 1] in operadores:
                formula[i + 1]
                print('Nada de errado até agora')
            else:
                print('Parece que você não atribuiu símbolo a um operador 2')
                break
    

def check_sintaxe():
    verif = 0
    for i in range(len(formula)-1):
        if formula[i] in operadores:
            if formula[i + 1] in letras or formula[i + 1] == '~' or formula[i + 1] in sim:
                formula[i + 1]
                verif += 1

            else:
                print('\nInválida. Tente novamente!')
                break

        elif formula[i] in letras:
            if formula[i + 1] == '~' or formula[i + 1] in sim or formula[i + 1] in operadores:
                formula[i + 1]
                verif += 1
            else:
                print('\nFórmula inválida! Tente novamente!')
                break
        elif formula[i] in sim:
            if formula[i + 1] in letras or formula[i + 1] == '~':
                formula[i + 1]
                verif += 1
            else:
                print('\nFórmula inválida! Tente novamente!')
                break

        elif formula[i] == '~':
            if formula[i + 1] == '~' or formula[i + 1] in sim or formula[i + 1] in operadores:
                verif += 1
            else:
                print('\nFórmula inválida! Tente novamente!')
                break

    if verif == len(formula)-1:
        print('\nFórmula Válida!')

c = 0
letrocas = list() #LISTA DE LETRAS USADAS PARA A TABELA

def tabela():
    for c in formula:
        if c in letras:
            letrocas.append(c)#ADD LETRAS EM LETROCAS


    print(ttg.Truths(letrocas))




def check_alfabeto():
    if set(formula).intersection(alfabeto):
            check_position()
    else:
        print('\nFórmula inválida!')

while op != 0:
    print('\n\nMENU DE OPERAÇÕES: \n'
          '1- Informe a fórmula para realizar as operações; \n'
          '2- Verifica se a fórmula é válida; \n'
          '3- Calcula o tamanho da fórmula;\n'
          '4- Mostra a tabela verdade;\n'
          '0- Fecha o programa.\n')

    op = int(input('Digite a operação desejada: '))

    if op == 1:

        print('\nREGRAS: \n'
              'O alfabeto usado será: P, Q e R; \n'
              'Os simbolos proposicionais são:\n'
              'Negação = ~\nOu,Or = v\nAnd, Conjução = ^\nSe, Implicação = >\nSe somente se = $\n'
              'Pode-se usar apenas uma vez cada símbolo de pontuação;\n'
              'O tamanho máximo de cada fórmula é de 12 caracteres (considerando também os símbolos).')

        formula = str(input('Digite a fórmula: '))

        if len(formula) > 12:
            print('Fórmula inválida!')

        else:
            print('\nA fórmula digitada é: ', formula)

    if op == 2:
        check_alfabeto()

    if op == 3:
        print('\nTamanho da fórmula é: ', len(formula))

    if op == 4:
        tabela()
