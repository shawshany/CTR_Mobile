#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-09-09 19:54
# @Author   : ora
# @E-mail   : victor.xsyang@gmail.com
# @File     : dataformatter.py
# @User     : ora
# @Software: PyCharm
# @Description: 
#Reference:**********************************************
import sys,os
sys.path.append(os.path.join('CTR_Mobile', os.path.dirname('__file__')))

import pandas as pd
from scipy import sparse

class DataFormatter():
    '''
    Defines and formats data for the Unicom dataset.
    '''
    def __init__(self,df,columns=None):
        '''

        :param df: DataFrame
        '''
        self.df = df
        self.columns = columns

    def get_dummies(self):
        return pd.get_dummies(self.df,columns=self.columns)


    def forward(self):
        df = self.get_dummies()
        return sparse.csr_matrix(df.values)

