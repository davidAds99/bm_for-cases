# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:24:45 2022

@author: William Prada
"""
import numpy as np
import pandas as pd


class FirstCases():
    """
    Class to create a main dataframe.
    """
    def __init__(self, df_base):
        """
        Read and transform to self a main dataframe.

        Parameters
        ----------
        df_base : DataFrame
            Dataframe will be a main datagframe.

        Returns
        -------
        None.

        """
        self.base = df_base

    def unique_values(self):
        """
        Save unique row in a dataframe

        Returns
        -------
        df_unique_values : DataFrame
            Dataframe with unique rows.

        """
        df_all_values = self.base
        df_unique_values = df_all_values.drop_duplicates()
        df_unique_values.to_csv('Data/unique_cases_BM.csv', index=False)
        return df_unique_values

class NewCases():
    """
    Class to add new rows to main dataframe.
    """
    def __init__(self, df_new):
        """
        Read and transform to self a new dataframe.

        Parameters
        ----------
        df_new : DataFrame
            Dataframe with differents rows of main dataframe.

        Returns
        -------
        None.

        """
        self.df_new = df_new

    def new_values(self):
        """
        Concatenation between dataframe main with unique values
        of new dataframe

        Returns
        -------
        df_new : DataFrame
            Show differents rows of main dataframe.
        df_main : DataFrame
            Dataframe with unique rows.

        """
        df_new = self.df_new
        df_main = pd.read_csv('Data/unique_cases_BM.csv',
                              low_memory=False,
                              index_col=False)

        if list(df_new.columns) !=  list(df_main.columns):

            print('Columns of are differents to main df')

        else:

            df_new = pd.merge(df_new, df_main, how='left', indicator='Exist')
            df_new['Exist'] = np.where(df_new.Exist == 'both', True, False)
            df_new_uv = df_new[df_new.Exist == False].drop_duplicates()

            df_main = pd.concat([df_main, df_new_uv[list(df_main.columns)]],
                                ignore_index=True)
            df_main.to_csv('Data/unique_cases_BM.csv', index=False)

        return df_new, df_main
