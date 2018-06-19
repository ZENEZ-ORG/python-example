# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 01:43:23 2018
@author: ZEN

Intro to Data Structures
http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
에 대한 요약
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 시리즈 기본형
# s = pd.Series(data, index=index)

d = np.random.randn(5)
s = pd.Series(d, index=['e', 'c', 'b', 'd', 'z'])

print(s)

# 시리즈 Dic형
# Dic형 시리즈는 자동으로 정렬됨
d = {'b' : 1, 'a' : 0, 'c' : 2}
s = pd.Series(d)

print(s)

# 시리즈간 data를 연산 할 수 있음
print(s * s)
print(s + s)
print(s + 10)

# numpy 매소드에 시리즈를 전달 할 수 있음
print(np.exp(s))

d = {'b' : np.random.randn(500), 'a' : np.random.randn(500), 'c' : np.random.randn(500)}
s = pd.Series(d)
print(s)

dx = pd.read_excel('sample.xls', 'Sheet1', index_col='date', na_values=['NA'])
print(dx.head())
#dxplt = dx[['l','m']].loc[['2018-04-12:02','2018-05-11:01']]
dx.plot(kind='line', y='l')
# 심화내용
# index가 서로 다른 두 Series간 연산 결과는 ?