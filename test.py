#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-09-09 19:54
# @Author   : ora
# @E-mail   : victor.xsyang@gmail.com
# @File     : test.py
# @User     : ora
# @Software: PyCharm
# @Description: 
#Reference:**********************************************
import sys,os
sys.path.append(os.path.join('CTR_Mobile', os.path.dirname('__file__')))

import pandas as pd

from utils.dataformatter import DataFormatter
from utils.utils import get_columns
from utils.utils import store_train_data

# read data
df_137W_user_behavior = pd.read_csv('20200806_137W_user_behavior.txt')
df_137W_user_behavior.columns = ['serierial_number','is_click','h5_click_nums','is_order','PRODUCT_ID']

df_704_user_behavior = pd.read_csv('20200806_704_user_behavior.txt')
df_704_user_behavior.columns = ['serierial_number','is_click','h5_click_nums','is_order','PRODUCT_ID']

df_440W_user_behavior = pd.read_csv('20200806_440W_user_behavior.txt')
df_440W_user_behavior.columns = ['serierial_number','is_click','h5_click_nums','is_order','PRODUCT_ID']

df_user_137w = pd.read_csv('user_137w.txt')
df_user_137w.columns = get_columns('data/columns_user.txt')

df_user_704 = pd.read_csv('user_704.txt')
df_user_704.columns = get_columns('data/columns_user.txt')

df_user_440w = pd.read_csv('user_440w.txt')
df_user_137w.columns = get_columns('data/columns_user.txt')

df_product_information = pd.read_csv('product_information.txt')
df_product_information.columns = get_columns('data/columns_product.txt')

# merge data
## df_137w+df_704+df_440w concat
df_user_behavior = pd.concat([df_137W_user_behavior,df_440W_user_behavior,df_704_user_behavior],axis=0)

## df_user_137w+df_user_137w+df_user_137w concat
df_user = pd.concat([df_user_137w,df_user_440w,df_user_704],axis=0)

#df_user_behavior、df_user、product merge
df_tmp = pd.merge(df_user_behavior,df_user,on='serierial_number',how='inner')
df_wide = pd.merge(df_tmp,df_product_information,on='PRODUCT_ID',how='inner')


data,label = XX

df_formater = DataFormatter(data)
df_wide_csr = df_formater.forward()

store_train_data(df_wide_csr,label,'data/train_data.txt')
