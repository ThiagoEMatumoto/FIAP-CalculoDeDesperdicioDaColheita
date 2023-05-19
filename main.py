# Thiago Eiji Matumoto
# RM 97711

# Tomando como base os dados fornecidos pelo texto, vamos considerar que em uma colheita Manual da cana-de-açúcar há uma
# perda de 5% e na colheita com Máquinas há uma perda de 15%.
#
# Baseado nestes dados, faça o algoritmo – Programa em Python – que digite a colheita (em toneladas) de cada mês de um ano,
# calcule a projeção de toneladas que serão desperdiçadas se colhidas manualmente ou através de máquinas e apresente estas projeções.
# Ao final das leituras e cálculos dos meses, deve-se exibir o total consolidado do ano das colheitas e das projeções de desperdício Manual e Maquinária.

import time
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    print(': ' * 40)
    print('  ' * 11 + 'CALCULADORA DE PERDA')
    print(': ' * 40)


def main():
    limpar_tela()
    title()

    mes = 1
    total_produzido = 0
    total_desperdicio_manual = 0
    total_desperdicio_maquina = 0
    espacos_mes = 10
    espacos_dados = 20
    text_perda_manual = 'Perda Manual'
    text_perda_maquina = 'Perda com Máquina'


    print('Insira as toneladas colhidas por mês:')
    while mes in range(1, 13, 1):
        try:
            text = f'Mês {mes}'
            producao = float(input(text.ljust(espacos_mes, '.') + ':'))

            if producao < 0:
                print("hey, por favor, insira um valor não negativo!")
                time.sleep(1.5)
                continue

            total_produzido += producao
            desperdicio_manual = producao * 0.05
            total_desperdicio_manual += desperdicio_manual
            desperdicio_maquina = producao * 0.15
            total_desperdicio_maquina += desperdicio_maquina

            print(f' ' * espacos_mes + text_perda_manual.ljust(espacos_dados, '.') + f': {desperdicio_manual:.2f}')
            print(f' ' * espacos_mes + text_perda_maquina.ljust(espacos_dados, '.') + f': {desperdicio_maquina:.2f}')
            mes += 1
        except ValueError:
            print("hey, por favor, apenas números!")
            time.sleep(2)
            limpar_tela()
            continue

    print('RELATÓRIO CONSOLIDADO: ')
    print(f'Colheita do ano'.ljust(espacos_dados, '.') + f': {total_produzido:.2f}')
    print('Projeção de desperdicio:')
    print(text_perda_manual.ljust(espacos_dados, '.') + f': {total_desperdicio_manual:.2f}')
    print(text_perda_maquina.ljust(espacos_dados, '.') + f': {total_desperdicio_maquina:.2f}')

    while True:
        try:
            deseja_retornar = input('Deseja realizar outro calculo da suas perdas ( [S]im ou [N]ão ): ')
            if deseja_retornar in 'Ss':
                main()
            elif deseja_retornar not in 'SsNn':
                print("hey, por favor, coloque uma entrada válida")
                time.sleep(2)
                limpar_tela()
            else:
                break
        except ValueError:
            print("hey, por favor, coloque uma entrada válida")
            time.sleep(2)
            limpar_tela()
            continue






if __name__ == '__main__':
    main()
