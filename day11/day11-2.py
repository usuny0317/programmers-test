"""
문제 설명
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

입출력 예
n	k	result
10	3	[3, 6, 9]
15	5	[5, 10, 15]
"""
def solution(n, k):
    answer = []
    for i in range(k,n+1,k):
        answer.append(i)
    return answer