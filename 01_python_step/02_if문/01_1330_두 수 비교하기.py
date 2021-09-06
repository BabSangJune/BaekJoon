"""
날짜 : 2021.08.01
학습 : BEAKJOON
제목 :
01_1330_두 수 비교하기

문제 :
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

입력 :
1) 1 2
2) 10 2

출력 :
1) <
2) >
"""

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')