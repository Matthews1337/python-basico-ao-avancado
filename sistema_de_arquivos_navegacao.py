"""
Sistemas de arquivos e navegação


Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso
do módulo os do Python.

os -> Operating System - Sistema Operacional

"""

# Fazer o import

import os

# getcwd -> Pega o current work directory - diretorio de trabalho corrente


print(f"O dietório de trabalho é: {os.getcwd()}") # Output: C:\Users\Matheus\Documents\PROGRAMACAO\PYTHON_ESTUDOS

os.chdir('..')


print(f"O dietório de trabalho é: {os.getcwd()}") # Output: C:\Users\Matheus\Documents\PROGRAMACAO\


# Para usuários Windows
# Cuidado ao verificar diretórios 

# print(os.path.isabs('C:\\Users\\geek'))

# Podemos identificar o sistema operacional com o módulo os

print(os.name) # Posix (Linux e Mac), nt (Windows)

# informando o path

caminho = os.path.join(os.getcwd(), 'geek')

print(caminho)

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()
arquivos = list(scanner)

print(arquivos)

scanner.close()