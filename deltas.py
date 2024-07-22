"""
Trabalhando com deltas de data e hora


delta == diferença

"""
import datetime

# data atual

dt_atual = datetime.datetime.now()


# CAlculando o delta para o meu aniversario

aniversario = datetime.datetime(2024, 10,15)

delta_tempo = aniversario - dt_atual

print(delta_tempo)

boleto_pago = datetime.datetime.now()

tempo_para_vencer = datetime.timedelta(days=3)

vencimento_boleto = boleto_pago + tempo_para_vencer
vencimento_boleto = vencimento_boleto.strftime('%d/%m/%Y')

print(f'O boleto vence no dia: {vencimento_boleto}')