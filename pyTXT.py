"""
Uma biblioteca básica para trabalhar com arquivos .txt

Sinta-se livre para realizar qualquer modificação a fim de
adequar ao seu projeto
"""


def lerTxt(nomeDoTxt):
    'Retorna uma lista com o conteúdo do .txt separado por linhas'
    txt = open(nomeDoTxt, 'r', encoding='UTF-8')
    conteudo = txt.readlines()
    txt.close()
    return conteudo


def gravarNoTxt(nomeDoTxt, novoConteudo):
    'Adiciona um novo conteúdo ao final do conteúdo já existente'
    conteudo = lerTxt(nomeDoTxt)
    txt = open(nomeDoTxt, 'w', encoding='UTF-8')
    txt.append((novoConteudo + '\n'))
    txt.writelines(conteudo)
    txt.close()


def atualizarTxt(nomeDoTxt, novoConteudo, antigoConteudo):
    'Procura por um conteúdo dado e substitui sua linha pelo novo'
    conteudo = lerTxt(nomeDoTxt)
    txt = open(nomeDoTxt, 'w', encoding='UTF-8')
    for linha in conteudo:
        if antigoConteudo in linha:
            conteudo[(conteudo.index(linha))] = novoConteudo + '\n'
    txt.writelines(conteudo)
    txt.close()
