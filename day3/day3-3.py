"""
입출력 예
my_string	k	result
"string"	3	"stringstringstring"
"love"	10	"lovelovelovelovelovelovelovelovelovelove"
"""
def solution(my_string, k):
    answer = ''
    for i in range(0,k,1):
        answer=answer+my_string
    return answer