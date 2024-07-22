"""
Dicionários

OBS: EM ALGUMAS LINGUAGENS DE PROGRAMAÇÃO, OS DICIONÁRIOS PYTHON SÃO CONHECIDOS COMO POR MAPAS


DICIONÁRIOS SÃO COLEÇÕES DO TIPO CHAVE/VALOR.

DICIONÁRIOS SÃO REPRESENTADOS POR CHAVES {}


print(type({})) # Classe Dicionário

OBS: SOBRE OS DICIONARIOS
    - Chave e valor sao separados por dois pontos (:) "Chave: Valor";
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;



# CRIAÇÃO DE DICIONARIOS
# FORMA 1 (MAIS COMUM)


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))



# FORMA 2 (MENOS COMUM)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))



# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])
  #print(paises['ru']) # OBS: CASO TENTAMOS FAZER UM ACESSO UTILIZANDO UMA CHAVE QUE NAO EXISTE, TEREMOS O ERRO KeyError


# FORMA 2 - Acessando via get - RECOMENDADA

print(paises.get('br'))
print(paises.get('ru')) # Tipo None


Tipo None

O tipo None em Python representa o tipo sem tipo, ou poderia ser conhecido tambem como tipo vazio.

OBS1: O tipo None é SEMPRE especificado com a primeira letra maiuscula

OBS2: O tipo None é SEMPRE conseiderado FALSO




russia = paises.get('ru')

if russia:
    print('encontrei o pais')
else:
    print('Nao encontrei o pais')

# PODEMOS DEFINIR UM VALOR PADRAO PARA CASO NAO ENCONTREMOS O OBJETO COM A CHAVE INFORMADA

pais = paises.get('ru', 'nao encontrei')

print(f'encontrei o pais {pais}')



# PODEMOS VERIFICAR SE DETERMINADA CHAVE EM UM DICIONARIO

print('br' in paises)
print('eua' in paises)
print('Estados Unidos ' in paises)


if 'ru' in paises:
    russia = paises['ru']




# PODEMOS UTILIZAR QUALQUER TIPO DE DADO (int, float, string, boolean), INCLUSIVE LISTA, TUPLA DICIONARIO, COMO CHAVES DE DICIONARIOS

# TUPLAS POR EXEMPLO SAO BASTANTE INTERESSANTES DE SEREM UTILIZADAS COMO CHAVE DE DICIONARIOS, POS AS MESMAS SAO IMUTAVEIS

localidades = {
    (35.6895, 39.5435): 'Escritorio em Tokyo',
    (40.3543, 74.4564): 'Escritorio em Nova York',
    (37.4533, 122.5434): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))




# ADICIONAR ELEMENTOS EM UM DICIONARIOS


receita = {'jan': 100, 'fev': 120, 'mar': 300}


# FORMA 1

receita['abr'] = 350

print(receita)


# FORMA 2

novo_dado = {'mai': 500}

receita.update(novo_dado)    #OU #  receita.update({'mai': 500})
print(receita)

# CONCLUSÃO 1: A FORMA DE ADICIONAR NOVOS ELEMENTOS OU ATUALIZAR DADOS EM UM DICIONARIO É A MESMA
# CONCLUSÃO 2: EM DICIONARIOS, NAO PODEMOS TER CHAVES REPETIDAS




# REMOVER DADOS DE UM DICIONARIO

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)


# FORMA 1 - MAIS COMUM
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: PRECISAMOS SEMPRE INFORMAR A CHAVE, E CASO NAO ENCONTRE O ELEMENTO, UM KEYERROR É RETORNADO

# OBS 2: AO REMOVERMOS UM OBJETO, O VALOR DESTE OBJETO É SEMPRE RETORNADO

# FORMA 2

del receita['fev']

print(receita)

# OBS: SE A CHAVE NAO EXISTIR SERA GERADO UM KEYERROR
# NESTE CASO O VALOR REMOVIDO NAO É RETORNADO




# IMAGINE QUE VOCE TEM UM COMERCIO ELETRONICO, ONDE TEMOS UM CARRINHO DE COMPRAS NA QUAL ADICIONAMOS PRODUTOS

# 1 - PODEMOS UTILIZAR UMA LISTA PARA ISSO? SIM!

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God Of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)



# 2 - PODEMOS UTILIZAR UMA TUPLA PARA ISSO? SIM!


produto1 = ('Playstation 4 ', 1, 2300.00)
produto2 = ('God Of War ', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)


# TERIAMOS QUE SABER QUAL O INDICE DE CADA INFORMAÇÃO NO PRODUTO

# 3 - PODEMOS UTILIZAR DICIONARIOS PARA ISSO? SIM!


carrinho = []

produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'nome': 'God Of War', 'Quantidade': 1, 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# DESTA FORMA, FACILMENTE ADICIONAMOS OU REMOVEMOS PRODUTOS NO CARRINHO E EM CADA PRODUTO

# PODEMOS TER A CERTEZA SOBRE CADA INFORMAÇÃO




# LIMPAR O DICIONARIO (ZERAR DADOS)

d.clear()
print(d)


# COPIANDO DICIONARIO PARA OUTRO DICIONARIO

# FORMA 1

novo = d.copy()

print(novo)

novo['d'] = 4 # DEEP COPY

print(d)
print(novo)



# FORMA 2 # SHALLOW COPY

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)



"""

# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}





# METODOS DICIONARIOS

# FORMA NAO USUAL DE CRIAÇAO DE DICIONARIOS

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O METODO fromkeys RECEBE DOIS PARAMETROS: UM ITERAVEL E UM VALOR
# ELE VAI GERAR PARA CADA VALOR DO ITERAVEL UMA CHAVE E IRA ATRIBUIR A ESTA CHAVE O VALOR INFORMADO

veja = {}.fromkeys('teste', 'valor')

print(veja)


veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)