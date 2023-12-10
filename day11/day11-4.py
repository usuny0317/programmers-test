"""
정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

입출력 예
start_num	end_num	result
10	3	[10, 9, 8, 7, 6, 5, 4, 3]
"""
def solution(start, end_num):
    answer = []
    for i in range(start, end_num-1,-1):
        answer.append(i)
    return answer