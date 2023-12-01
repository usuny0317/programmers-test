"""
입출력 예
a	b	flag	result
-4	7	true	3
-4	7	false	-11
"""
def solution(a, b, flag):
    answer = 0
    if flag:
        answer=a+b
    else:
        answer=a-b
    return answer