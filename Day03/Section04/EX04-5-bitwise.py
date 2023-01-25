'''
비트 연산자
    어떤 변수의 값을 0과 1의 조합인 2진수,
    즉 비트로 변환한 뒤에 비트단위로 연산 수행

    1. &(AND) : 입력이 모두 1,아니면 0
    2. |(OR) : 입력중 하나라도 1이면 1,아니면 0
    3. ^(XOR) : 입력이 서로 다르면 1, 아니면 0 (이스클루시아
    4. ~(NOT) :입력이 0이면 1, 입력이 1이면 0
    5. <<( SHIFT : 비트 단위로 왼쪽으로 N비트 이동하며
                   2의 N거듭 제곱만큼 곱셈
    5. >>( SHIFT : 비트 단위로 오른쪽로 N비트 이동하며
                   2의 N거듭 제곱만큼 나숫셈
'''
a = 6                               #   0110 ->  6
b = 5                               #   0101 ->  5
print('a & b : {}'.format(a & b))   #   0100 ->  4 둘다 같아야 true
print('a | b : {}'.format(a | b))   #   0111 ->  7 둘중 하나라도 같으면 true
print('a ^ b : {}'.format(a ^ b))   #   0011 ->  3 서로 달라야 true
print('~b : {}'.format(~b))         #(1)1010 -> -6 2의 보수(2진법 반전 후  +1비트)
print('a << 1 : {}'.format(a << 1)) #   1100 -> 12 비트를 왼쪽으로 n칸 옮긴다
print('a >> 1 : {}'.format(a >> 1)) #   0011 ->  3 비트를 오른쪽으로 n칸 옮긴다

