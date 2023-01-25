'''
반복문
    어떤 수행 작업을 한번이 아니라 계속 해서 수행 해야 할 때 사용한다.

반복문 종류
    while, for문
    
while문 
    특정 조건을 만족하는 동안 반복 해서 수행하는 코드

변수 (초기화)
while 조건식:
    반복 실행코드

'''

n = 10
while n >= 1:
    print(n) # n = 0일때 거짓이기 때문에 멈춤
    n -= 1

print("while 끝나고 n 값 : {}".format(n))