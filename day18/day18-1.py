"""
문제 설명
문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때
나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

입출력 예
myString	result
"oxooxoxxox"	[1, 2, 1, 0, 1, 0]
"xabcxdefxghi"	[0, 3, 3, 3]
"""
def solution(myString):
    answer = []
    last=0
    for i in range(0,len(myString),1):
        if myString[i]=="x":
            answer.append(i-last)
            last=i+1
        if i==len(myString)-1:
            answer.append(i-last+1)
    return answer