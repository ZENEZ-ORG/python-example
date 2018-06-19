# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:18:06 2018

@author: ZEN-1
"""
#import random
import sqlite3
conn = sqlite3.connect('company.db')
curs = conn.cursor()
#curs.execute('create table employee (name, age)')
#curs.execute("insert into employee values ('Ali', 28)")
#values = [('Brad',54), ('Ross', 34), ('Muhammad', 28), ('Bilal', 44)]

for i in range(1, 5200):
    values = [('any', i, i/2, i/3, i/4, i*10)]
    curs.executemany('insert into employee values(?, ?, ?, ?, ?, ?)', values)

conn.commit()
conn.close()