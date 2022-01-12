# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:14:55 2022

@author: Asus
"""

import pandas as pd
from unique_cases_bm import FirstCases, NewCases

#Create a DataFrame
d = {'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine',
            'Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
            'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
            'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}

df = pd.DataFrame(d,columns=['Name','Age','Score'])

#test dataframe
dict_test = {'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine',
            'Alisa','Bobby','kumar','Alisa','Alex','Cathrine','Esteban','Valeri','David','David'],
            'Age':[26,24,23,22,23,24,26,24,22,23,24,24,15,13,23,23],
            'Score':[85,63,55,74,31,77,85,63,42,62,89,77,88,90,85,85]}

df_test = pd.DataFrame(dict_test,columns=['Name','Age','Score'])

test_fc = FirstCases(df).unique_values()
test_nc, test_main_df = NewCases(df_test).new_values()
