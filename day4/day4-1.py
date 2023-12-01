"""
입출력 예
num	n	result
98	2	1
34	3	0
"""

def solution(num, n):
    answer = 0
    if num%n==0:
        answer=1
    return answer