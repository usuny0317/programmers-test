"""
문제 설명
정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
단, arr에 2가 없는 경우 [-1]을 return 합니다.


입출력 예
arr	result
[1, 2, 1, 4, 5, 2, 9]	[2, 1, 4, 5, 2]
[1, 2, 1]	[2]
[1, 1, 1]	[-1]
[1, 2, 1, 2, 1, 10, 2, 1]	[2, 1, 2, 1, 10, 2]
"""
def solution(arr):
    answer = []
    min = 0
    max = 0
    for i in range(0, len(arr) - 1, 1):
        if arr[i] == 2:
            min = i
            break
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == 2:
            max = i
            break
    if max == 0 and min == 0:
        answer.append(-1)
    elif min == max:
        answer = (arr[min:min + 1])
    else:
        answer = (arr[min:max + 1])

    return answer