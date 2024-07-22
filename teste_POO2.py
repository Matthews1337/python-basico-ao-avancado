from teste_POO import Df_, Df_2
import pandas as pd


csv = pd.read_csv('../data/test.csv')

# print(csv)




aux_saude = Df_()

aux_saude1= aux_saude.open_df('../data/test.csv')

# print(aux_saude1)






aux_saude2 = Df_2(df_path='../data/test.csv')

print(aux_saude2.open_dataframe())