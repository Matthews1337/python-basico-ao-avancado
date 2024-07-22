"""
manipulando data e hora

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime



"""

import datetime

# print(dir(datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)



# Retorna data e hora corrente

print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minute, seconds, miliseconds)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas, 0 minutos, 0 segundos

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)


tempo_datetime = datetime.datetime(2019, 1, 1,0)

tempo_string = "01/01/2019"
tempo_string = tempo_string.split("/")

tempo_formatado = datetime.datetime(int(tempo_string[2]), int(tempo_string[1]), int(tempo_string[0]))

print(tempo_formatado)


# Acessando individualmente os elementos de data e hora

print(tempo_formatado.year)
print(tempo_formatado.month)
print(tempo_formatado.day)

print(dir(tempo_formatado)) # para saber o que podemos usar 