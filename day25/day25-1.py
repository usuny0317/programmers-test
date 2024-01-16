"""
문제 설명
양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
n	result
4	[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
5	[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
"""


def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0] * n for _ in range(n)]

    k = 0
    j = 0
    go = "r"
    # k 그 j 증 (오른쪽) // k 증 j 그 (아래) // k 그 j 감 (왼쪽) //k 감 j 그 (위로) 반복...
    for i in range(n * n):
        answer[k][j] = i + 1
        if go == "r":
            j = j + 1
            if j == n - 1 or answer[k][j + 1] != 0:
                go = "d"
        elif go == "d":
            k = k + 1
            if k == n - 1 or answer[k + 1][j] != 0:
                go = "l"
        elif go == "l":
            j = j - 1
            if j == 0 or answer[k][j - 1] != 0:
                go = "u"
        elif go == "u":
            k = k - 1
            if k == n - 1 or answer[k - 1][j] != 0:
                go = "r"
    return answer