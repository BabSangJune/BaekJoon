"""
날짜 : 2021.08.01
학습 : BEAKJOON
제목 : 10_10430_ 나머지
문제 :
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

입력 :
5 8 4

출력 :
1
1
0
0
"""

a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)