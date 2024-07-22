"""
Sistema de arquivos - Manipulação


"""

import os
# Descobrindo se um arquivo ou diretorio existe

# Arquivo

# Paths relativos

# print(os.path.exists("teste.txt")) # True
# print(os.path.exists("outro.txt")) # False


# Paths Absolutos

print(os.path.exists("C:/Users/Matheus/Documents/PROGRAMACAO/PYTHON_ESTUDOS/Python_Estudy/Udemy/teste.txt")) # True


# Criando arquivos
# forma 1
# open('arquivo-teste.txt', 'w').close()

# os.mknod("arquivo_teste.txt") 
# os.mknod("C:/Users/Matheus/Documents/PROGRAMACAO/PYTHON_ESTUDOS/Python_Estudy/Udemy/arquivo_teste.txt")

#OBS: Se vc estiver usando no Mac OS, pode haver um erro de PermissionError

# OBS: Criando um arquivo via mknod() se o arquivo ja existir teremos o erro FileExistsError

# Criando diretorios

os.mkdir("teste_diretorio")
# os.mkdir("C:/Users/Matheus/Documents/PROGRAMACAO/PYTHON_ESTUDOS/Python_Estudy/Udemy/arquivo_teste.txt")


# Renomear arquivos e diretorios

# Arquivos

os.rename("teste.txt", "testee.txt")

# Deletar

# ATENÇÃO!!! Cuidado com os comandos de deleção, Ao deletarmos um arquivo ou diretorio, eles não vão para a lixeira. ELes somem

# os.remove("testee.txt")

# OBS: Se o arquivo estiver aberto e tentar deletar, irá dar erro
# OBS: Caso o arquivo não exista, teremos o FileNotFoundError
# OBS: Se informar um diretório e não um arquivo, teremos um IsADirectoryError



# removendo diretorios

os.rmdir("nome_do_diretorio")

# OBS: Se o diretório tiver qualquer conteúdo,teremos um OSError
