# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:57:33 2018

@author: ZEN-1
"""
import time
start_time = time.time() 

def loop(len1, len2):
	for i in range(len1):
		for j in range(len2):
			if i == (len1-1) and j == (len2-1):
				print ("End For Loop!")
loop(10000, 1000)

print("start_time", start_time) #출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
print("--- %s seconds ---" %(time.time() - start_time))