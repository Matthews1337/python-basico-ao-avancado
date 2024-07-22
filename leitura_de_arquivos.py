"""
Para ler o conteúdo de um arquivo em Python , utilizamos a função integrada open(), que significa 'abrir'


open() -> na forma mais simples de utilização nós passamos apenas um parâmetro de entrada , que neste caso é o nome do arquivo a ser lido. 
Essa função retorna um _io. TextIOWrapper e é com ele que trabalhamos então


OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então, teremos o erro FileNotFoundError

O texto só vai ser retornado após o uso do metodo read()

OBS: Ao trabalhar com arquivos após o a leitura e realizado os trabalhos com o arquivo, devemos fechar a conexão com o método close()


OBS: Se tentarmos manipular o arquivo após o seu fechamento, teremos um ValueError

"""

# Exemplo

arquivo = open('teste.txt', encoding='UTF-8').read()
arquivo_list = arquivo.split('\n')
arquivo_list.close()




print(arquivo_list)

