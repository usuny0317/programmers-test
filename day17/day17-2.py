"""
문제 설명
문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

입출력 예
myString	pat	result
"banana"	"ana"	2
"aaaa"	"aa"	3
"""
def solution(myString, pat):
    count = 0
    a= myString.find(pat)
    b=len(pat)
    for i in range(a,len(myString),1):
        if myString[i:i+b]==pat:
            count=count+1
    return count