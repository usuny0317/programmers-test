"""
문제 설명
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

입출력 예
num_list	result
[3, 4, 5, 2, 1]	1
[5, 7, 8, 3]	0
"""
def solution(num_list):
    answer = 0
    a=1
    b=0
    for i in num_list:
        a=a*i
        b=b+i
    if a<(b*b):
        answer=1
    elif a>(b*b):
        answer=0
    return answer