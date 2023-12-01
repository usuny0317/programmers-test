"""
입출력 예
number	n	m	result
60	2	3	1
55	10	5	0
"""
def solution(number, n, m):
    answer = 0
    if (number%n==0)and (number%m==0):
        answer=1
    return answer