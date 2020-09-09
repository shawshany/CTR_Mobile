#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-09-09 22:26
# @Author   : ora
# @E-mail   : victor.xsyang@gmail.com
# @File     : utils.py
# @User     : ora
# @Software: PyCharm
# @Description: 
#Reference:**********************************************
import sys,os
sys.path.append(os.path.join('CTR_Mobile', os.path.dirname('__file__')))
def get_columns(path):
    with open('path','r') as f:
        data = f.readlines()
    data_ = None
    for value in data:
        data_.append(value.strip())
    return data_

"""
is the standard CSR representation 
where the column indices for row i are stored in 
indices[indptr[i]:indptr[i+1]] and 
their corresponding values are stored in 
data[indptr[i]:indptr[i+1]]. 
"""
def store_train_data(csr_matrix,label,path):
    '''

    :param csr_matrix:
    :param label: list
    :param path:
    :return:
    '''
    m,n = csr_matrix.shape
    f = open('path', 'w')
    for i in range(m):
        column_indices = csr_matrix.indices[csr_matrix.indptr[i]:csr_matrix.indptr[i+1]]
        column_values = csr_matrix.data[csr_matrix.indptr[i]:csr_matrix.indptr[i+1]]
        f.write(str(label[i]))
        for i in range(len(column_indices)):
            f.write(' '+str(column_indices[i])+":"+str(column_values[i]))
        f.write('\n')
    f.close()