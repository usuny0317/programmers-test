"""
문제 설명
n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

입출력 예
arr	result
[[5, 192, 33], [192, 72, 95], [33, 95, 999]]	1
[[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]	0
"""
def solution(arr):
    answer = 1
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i][j]!=arr[j][i]:
                answer=0
                break
    return answer