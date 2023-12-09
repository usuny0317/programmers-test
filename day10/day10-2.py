"""
문제 설명
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	is_prefix	result
"banana"	"ban"	1
"banana"	"nan"	0
"banana"	"abcd"	0
"banana"	"bananan"	0
"""
def solution(my_string, is_prefix):
    answer = 0
    a=[]
    for i in range(len(my_string),1,-1):
        a.append(my_string[0:i])
    a.sort()
    if is_prefix in a:
        answer=1
    return answer