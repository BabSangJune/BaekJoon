"""
날짜 : 2021.08.01
학습 : BEAKJOON
제목 : 11_2588_곱셈
문제 :
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다

입력 :
5 8 4

출력 :
1
1
0
0
"""

a = int(input())
b = input()

# print(a * int(b[2]))
# print(a * int(b[1]))
# print(a * int(b[0]))
# print(a * int(b))

for i in b[::-1]:
    print(a * int(i))

print(a*int(b))

