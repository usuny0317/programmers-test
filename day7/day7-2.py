"""
문제 설명
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

입출력 예
l	r	result
5	555	[5, 50, 55, 500, 505, 550, 555]
10	20	[-1]
"""
def solution(l, r):
    answer = []
    for i in range(l,r+1,1):
        if "1" not in str(i):
            if "2" not in str(i):
                if "3" not in str(i):
                    if "4" not in str(i):
                        if "6" not in str(i):
                            if "7" not in str(i):
                                if "8" not in str(i):
                                    if "9" not in str(i):
                                        answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return answer

#다른 사람 풀이
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]

#set으로 안에 포함된거 정렬할 수 있는 것 같다.
# 정렬한게 05 뺐을 때 남이있지 않으면. 추가하기 