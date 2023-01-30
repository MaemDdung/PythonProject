'''
표준모듈
    파이썬에서 기본적으로 설치되어 있는 모듈

random - 난수 생성 모듈
    
'''
import random

# 두 인수 사이 난수
print(random.randint(1,10)) # 1 ~ 10

# range 함수 비슷
print(random.randrange(10)) # 0 ~ 10
print(random.randrange(1, 10)) # 0 ~ 9
print(random.randrange(1,10,2)) #1 ~ 9 홀수만 , 1+2 증감 


# 0이상 1미만
print(random.random())

if random.random() < 0.5: #50% 확률로 안녕하세요가 나옴
    print("안녕하세요")


#chioce함수 -리스트에서 랜덤
season = ['spring','summer', 'fall', 'winter']
print(random.choice(season))

#shuffle()함수 - 임의로 섞는 함수
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)