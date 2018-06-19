import serial
import sqlite3
import time

# 아두이노 Serial 출력과 파이썬 Serial 입력 주기가 같아야 함.
# 다르면 시간과 데이터 불일치 됨.. 아두이노, Serial, 파이썬, SQlite 모두 부담없는 속도로 정할 것.
insert_delay = 1

conn = sqlite3.connect('arduino.db')
curs = conn.cursor()
arduino = serial.Serial('COM6', 9600)


# 이정도 예외 처리로는 너무 부족. 꼼꼼하게 예외 처리 해줘야 함.
try:
    while 1:
        msg = arduino.readline()
        # 반드시 decode()하고 자료형 cast하고 제3의 변수에 저장할 것
        s1 = int(msg.decode())
        # sqlite datetime 형식에 맞게 문자열 생성
        timesqlite = time.strftime("20%y-%m-%d %H:%M:%S")
        # 센서값은 정수형인데 부동소수로 바꿔서 입력해봄, table 자료형 무시하고 입력됨
        # round() 반올림 함수
        # record 한줄식 입력 할 때는 (, , ,) 튜플형
        # record 여러개 batch 입력 할 때는 [(, , ,)] 리스트형. 아니면 오류남
        values = (timesqlite, round(s1, 2), round(s1/2, 2), round(s1/3, 2), 'asd')
        # 주의. values 자료형에 따라 curs.execute 명령 다름.
        curs.execute('insert into sensor values(?, ?, ?, ?, ?)', values)
        # 아래 코드는 표준시 입력
        # curs.execute('insert into sensor values(CURRENT_TIMESTAMP, ?, ?, ?, ?)', values)
        # 아래 코드는 한국 표준시, db에 직접 명령하면 작동되는데 프로그램 커서에서 작동안됨
        # curs.execute('insert into sensor values((CURRENT_TIMESTAMP, +9 hours), ?, ?, ?, ?)', values)
        conn.commit()
        s1 = 0 # 초기화, 다름 루프에서 쓰레기 값 입력 방지
        print(values)
        time.sleep(insert_delay)
except:
    # close() 안하고 팅기면 아두이노 먹통됨
    conn.close()
    arduino.close()
    print('#####팅겼음#####')
finally:
    conn.close()
    arduino.close()
    print('종료')