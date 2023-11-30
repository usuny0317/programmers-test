"""
입출력 예
a	b	result
2	91	364
91	2	912
"""
def solution(a, b):
    answer = 0
    ab=str(a)+str(b)
    ba=2*a*b
    if int(ab)>=ba:
        answer=int(ab)
    else:
        answer=ba
    return answer