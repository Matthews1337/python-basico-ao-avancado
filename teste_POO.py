import pandas as pd

class Df_:
    def __init__(self):
        self.dataframe_ = None


    def open_df(self, filepath):

        dataframe1 = pd.read_csv(filepath)

        self.dataframe_ = dataframe1
        return self.dataframe_
    

    def get_df_(self):
        return self.df_
    


class Df_2:
    def __init__(self, df_path):
        self.dataframe__ = df_path



    def open_dataframe(self):
        dataframe1 = pd.read_csv(self.dataframe__)
        return dataframe1