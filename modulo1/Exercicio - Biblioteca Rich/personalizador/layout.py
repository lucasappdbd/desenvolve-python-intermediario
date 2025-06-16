import os

from rich import print
from rich.layout import Layout

def verificaArquivo(texto):
    """Verifica se o texto digitado é o nome de um arquivo de texto."""

    global isArquivo
    extensao = str(texto[-3] + texto[-2] + texto[-1])

    if extensao == "txt" or extensao == "TXT":
        isArquivo = True
        return (f"{texto} [green]é o nome de um arquivo de texto")
    else:
        isArquivo = False
        return (f"{texto} [red]não é o nome de um arquivo de texto")


def abrirArquivo(texto):
    """Tenta exibir o conteúdo do arquivo, caso o texto digitado seja o nome de um arquivo de texto.
    
    O conteúdo do arquivo é exibido no lado direito do terminal.
    """

    arquivoExiste = os.path.isfile(texto)

    layout_terminal = Layout()
    layout_terminal.split_row(
        Layout(name="esquerda"),
        Layout(name="direita")
    )

    # Lado esquerdo: resultado da verificação
    
    layout_terminal["esquerda"].update(verificaArquivo(texto))

    # Lado direito: conteúdo do arquivo ou erro

    if arquivoExiste:
        f = open(texto, 'r')
        linhas = f.readlines()
        lista_linhas = []
        for i in range(len(linhas)):
            lista_linhas.append(linhas[i])
        f.close()

        conteudo_arquivo = "".join(lista_linhas)
        layout_terminal["direita"].update(conteudo_arquivo)
    else:
        caminho = os.path.abspath(texto)
        mensagem_erro = f"[yellow]{texto} [red]não foi encontrado no caminho [white]{caminho}"
        layout_terminal["direita"].update(mensagem_erro)

    print(layout_terminal)