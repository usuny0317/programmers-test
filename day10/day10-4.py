"""
문제 설명
문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을
문자열로 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	m	c	result
"ihrhbakrfpndopljhygc"	4	2	"happy"
"programmers"	1	1	"programmers"
"""


def solution(my_string, m, c):
    answer = ''
    colum = len(my_string) // m
    row = m
    array2 = [[0 for _ in range(row)] for _ in range(colum)]

    b = []
    for i in range(0, len(my_string), 1):
        b.append(my_string[i:i + 1])

    for k in range(0, colum, 1):
        for j in range(0, row, 1):
            array2[k][j] = b[0]
            b.remove(b[0])

    for k in range(0, colum, 1):
        answer = answer + array2[k][c - 1]
    return answer

#다른 사람 코드

def solution(s, m, c):
    return s[c-1::m]

#s 문자열을 m글자씩 나눴을 때 (한줄에 m개) 매 줄 마다 c-1 번째에(0~m-1) 있는 거 내놓기
#ex) a="1234567890" a[1::2] --> "24680"
# 12 34 56 78 90 으로 나뉘는데 매 묶음마다 인덱스 값 1인 친구 "2" "4" ... "0"

