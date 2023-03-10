'''
문자열(string)
    하나 이상 연속된 문자(character)들의 나열
    파이썬에서 문자열 자료형은 큰따옴효(" ")
    또는 작은 따옴표(' ') 사이에 위치
'''

#'hello'와 "hello"동일
print('hello' == "hello")

#변수의 문자열 할당
a = "hello"
print("hello")

#
b = """피카츄, 라이츄, 파이리, 꼬부기
버터플, 야도란, 
"""
print(b)

'''
문자 배열 => 문자열
    문자열 인덱싱(indexing)
    h   e   l   l   o => 문자열
    0   1   2   3   4 => 인덱스
   -5  -4  -3  -2  -1 => 마이너스 인덱스
'''

a = "hello"
print(a[1])
print(a[1]==a[-4])

'''
문자열 슬라이싱
    슬라이스 구문을 사용하여 문자 범위를 반환 할 수 있다.
    문자열의 일부를 반환하려면 시작 인덱스와 끝 인데스를 콜론으로 구분
'''
#인덱스 2부터 4까지 슬라이스
b = "Hello, World"
print(b[2:5])
#인덱스 0부터 처음부터 슬라이스
print(b[:5])
#인덱스 2부터 끝까지 슬라이스
print(b[2:])

a = "Hello, World"
#대문자
print(a.upper())
#소문자
print(a.lower())

#무자열 바꾸기
#H를 J로 바꾸기
print(a.replace("H", "J"))

#문자열 합
a = "Hello"
b = "World"
c = a+b
print(c)

#
a = "Age"
b = 15
c = a + " / " + str(b)
print(c)

