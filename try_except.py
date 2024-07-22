"""
Utiliza-se o bloco try except para fazer tratamento de erros que podem ocorrer no código.
 Previnindo assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas


 try:
    // execução do codigo
 except:
    //o que deve ser feito em caso de erro    

"""


# try:
#     nome()
# except:
#     print("Erro: Função não definida")


try:
    len(5)
except TypeError as e:
    print(f"Erro: {e}")