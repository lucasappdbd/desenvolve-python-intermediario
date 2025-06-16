import os

from rich import console
from rich import theme

tema = theme.Theme({
    "conteudo": "blue",
    "verificacao": "yellow",
    "nao_encontrado": "red"
})
console = console.Console(theme=tema)

def verificaArquivo(texto):
    """Verifica se o texto digitado é o nome de um arquivo de texto."""

    global isArquivo
    extensao = str(texto[-3] + texto[-2] + texto[-1])

    if extensao == "txt" or extensao == "TXT":
        isArquivo = True
    else:
        isArquivo = False

    if isArquivo:
        console.print(f"{texto} [green]é o nome de um arquivo de texto.", style="verificacao")
    else:
        console.print(f"{texto} [red]não é o nome de um arquivo de texto.", style="verificacao")


def abrirArquivo(texto):
    """Tenta exibir o conteúdo do arquivo, caso o texto digitado seja o nome de um arquivo de texto.
    
    Exibe o conteúdo do arquivo estilizado.
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

        console.print("\n[magenta]Conteúdo do arquivo:")

        console.print(f"{conteudo_arquivo}", style="conteudo")
    else:
        console.print(f"{texto} não foi encontrado no caminho {os.path.abspath(texto)}", style="nao_encontrado")