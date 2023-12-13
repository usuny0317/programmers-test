"""
문제 설명
정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때,
홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

입출력 예
num_list	result
[4, 2, 6, 1, 7, 6]	17
[-1, 2, 5, 6, 3]	8
"""
def solution(num_list):
    answer = 0
    w=0
    g=0
    for i in range(1,len(num_list)+1,1):
        if i%2==0:
            w=w+num_list[i-1]
        else:
            g=g+num_list[i-1]
    if w>g:
        answer=w
    elif g>w:
        answer=g
    else: answer=w
    return answer