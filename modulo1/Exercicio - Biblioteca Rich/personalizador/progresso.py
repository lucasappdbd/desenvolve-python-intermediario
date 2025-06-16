import os
import time

from rich import print
from rich import progress

def verificaArquivo(texto):
    """Verifica se o texto digitado é o nome de um arquivo de texto.
    
    Exibe uma barra de progresso simulando o processamento da verificação.
    """
    
    global isArquivo
    extensao = str(texto[-3] + texto[-2] + texto[-1])

    for i in progress.track(range(10), description="Verificando..."):
        time.sleep(0.2)  # Simulando o processamento da verificação    

    if extensao == "txt" or extensao == "TXT":
        isArquivo = True
    else:
        isArquivo = False

    if isArquivo:
        print (f"\n{texto} [green]é o nome de um arquivo de texto.")
    else:
        print (f"\n{texto} [red]não é o nome de um arquivo de texto.")


def abrirArquivo(texto):
    """Tenta exibir o conteúdo do arquivo, caso o texto digitado seja o nome de um arquivo de texto.
    
    Exibe o conteúdo do arquivo formatado.
    """

    arquivoExiste = os.path.isfile(texto)

    if arquivoExiste:
        f = open(texto, 'r')
        linhas = f.readlines()
        lista_linhas = []
        for i in range(len(linhas)):
            lista_linhas.append(linhas[i])
        f.close()

        conteudo_arquivo = "".join(lista_linhas)

        print("\n[magenta]Conteúdo do arquivo:")

        print(f"{conteudo_arquivo}")
    else:
        print(f"\n[yellow]{texto} [red]não foi encontrado no caminho [white]{os.path.abspath(texto)}")