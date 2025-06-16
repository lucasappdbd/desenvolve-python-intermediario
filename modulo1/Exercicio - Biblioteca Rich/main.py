"""Este script verifica se o texto digitado é o nome de um arquivo de texto

Em caso positivo, verifica se o arquivo existe no diretório de execução do script.
"""

import argparse

from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('texto', nargs='?')
    parser.add_argument('-a', '--arquivo', help='Informe o nome do arquivo')
    parser.add_argument('-m', '--modulo', type=int, choices=range(1,5), help='Módulos disponíveis: (1-Layout, 2-Painel, 3-Progresso, 4-Estilo )')
    parser.add_argument('-f', '--funcao', type=int, choices=range(1,3), help='Funções disponíveis: (1-Verificar se é nome de arquivo, 2-Abrir arquivo)')

    args = parser.parse_args()

    if args.texto == None:
        args.texto = args.arquivo

    extensao = str(args.texto[-3] + args.texto[-2] + args.texto[-1])

    modulos = [layout, painel, progresso, estilo]

    modulo = args.modulo
    if args.modulo == None:
        args.modulo = 2
        modulo = args.modulo

    # Exibe o resultado da verificação conforme as opções e parâmetros fornecidos pelo usuário
    if args.funcao == 1:
        modulos[modulo-1].verificaArquivo(args.texto)
    elif args.funcao == 2:
        modulos[modulo-1].abrirArquivo(args.texto)
    else:
        modulos[modulo-1].verificaArquivo(args.texto)
        modulos[modulo-1].abrirArquivo(args.texto)

if __name__ == '__main__':
    main()