"""
입출력 예
n	result
7	16
10	220
"""


def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(0, n + 1, 1):
            if (i % 2 == 0):
                answer = answer + (i * i)
    else:
        for i in range(0, n + 1, 1):
            if (i % 2 != 0):
                answer = answer + i

    return answer