"""
Métodos de data e hora

Com now() podemos especificar um timezone (fuso horario)


"""
import datetime

agora = datetime.datetime.now()

print(agora)

hoje = datetime.datetime.today()

print(hoje)



# mudanças ocorrendo à meia noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao) # output: 2024-07-10 00:00:00
print(repr(manutencao)) # output: datetime.datetime(2024, 7, 10, 0, 0)



# encontrar o dia da semana usando weekday()
# Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira

"""
0 - Segunda - feira ( Monday )
1 - Terça - feira ( Tuesday )
2 - Quarta - feira ( Wednesday )
3 - Quinta - feira ( Thursday )
4 - Sexta - feira ( Friday )
5 - Sábado ( Saturday )
6 - Domingo ( Sunday )

"""

print(manutencao.weekday())


# Descobrindo o dia da semana do meu nascimento
print("==========================================")
niver = '15/10/1997'
dia , mes, ano = (niver.split('/'))

aniversario = datetime.datetime(year=int(ano), month=int(mes), day=int(dia))


if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo')
else:
    print('dia inválido')


# Transformando datas/horas com strftime() (String format time)


data = datetime.datetime.now()

# data = data.strftime('%d/%B/%Y') # mes por extenso
# data = data.strftime('%d/%b/%Y') # mes por extenso abreviado
data = data.strftime('%d/%m/%y') # ano abreviado


print(data)



# Transformando string para datetime usando strptime()

nascimento = datetime.datetime.strptime('15/10/1997', '%d/%m/%Y')

print(nascimento)



# Somente HORA

almoco = datetime.time(12, 30, 0)
print(almoco)