import os

from rich import print
from rich import panel

def verificaArquivo(texto):
    """Verifica se o texto digitado é o nome de um arquivo de texto."""

    global isArquivo
    extensao = str(texto[-3] + texto[-2] + texto[-1])

    if extensao == "txt" or extensao == "TXT":
        isArquivo = True
        print(panel.Panel(f"{texto} [green]é o nome de um arquivo de texto", title="[blue]Verificar arquivo de texto"))
    else:
        isArquivo = False
        print(panel.Panel(f"{texto} [red]não é o nome de um arquivo de texto", title="[blue]Verificar arquivo de texto"))

def abrirArquivo(texto):
    """Tenta exibir o conteúdo do arquivo, caso o texto digitado seja o nome de um arquivo de texto.
    
    O conteúdo do arquivo é exibido dentro de um painel.
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
        print(panel.Panel(f"{conteudo_arquivo}", title=f"[magenta]Conteúdo do arquivo:", subtitle="Fim"))
    else:
        print(panel.Panel(f"[yellow]{texto} [red]não foi encontrado no caminho [white]{os.path.abspath(texto)}"))