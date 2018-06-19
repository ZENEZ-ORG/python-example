# -*- coding: utf-8 -*-

import get_time as gt

""" 반환값 순서대로
년, 월, 일, 시, 분, 초 정수형 리스트
년, 월, 일, 시, 분, 초 문자열형 리스트
부동소수점 초
"""
ti, ts, tsql = gt.get_time()

print(ti, type(ti)) # 정수형 리스트
print(ts, type(ts)) # 문자열 리스트
print(tsql, type(tsql))
#print(s, type(s)) # 부동소숫점 리스트

gt.time.sleep(1) # get_time은 time을 상속받았으므로 time의 sleep 함수를 끌어다 사용 가능

#시간의 차이를 초로 계산
#ti, ts, s2 = gt.get_time()
#print(s2 - s)

#년,월 출력
print(ts[0]+ts[1])
print(gt.time.strftime("%y%m"))

#시, 분, 초 출력
print(ts[3]+ts[4]+ts[5])
print(gt.time.strftime("%H%M%S"))