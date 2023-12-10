"""
문제 설명
문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는
인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	indices	result
"apporoograpemmemprs"	[1, 16, 6, 15, 0, 10, 11, 3]	"programmers"
"""
def solution(my_string, indices):
    indices.sort()
    j=0
    for i in indices:
        my_string=my_string[:i-j]+my_string[i+1-j:]
        j=j+1
    return my_string