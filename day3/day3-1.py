"""
입출력 예
str1	str2	result
"aaaaa"	"bbbbb"	"ababababab"
"""


def solution(str1, str2):
    answer = ''

    for i in range(0, len(str1), 1):
        answer = answer + str1[i:i + 1]
        answer = answer + str2[i:i + 1]

    return answer