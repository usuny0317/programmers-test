"""
문제 설명
문자열 배열 strArr이 주어집니다. strArr의 원소들을 길이가 같은 문자열들끼리
그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

입출력 예
strArr	result
["a","bc","d","efg","hi"]	2
"""
from collections import Counter

def solution(strArr):
    answer = 0
    k=[]
    for i in strArr:
        k.append(len(i)) #K에 각 요소의 길이 저장

    c = Counter(k) #k 관련 셈
    mode = c.most_common(1) #가장 많이 나온 요소 mode에 저장
    answer= mode[0][1] #[0][0]: 항목 [0][1]:개수 인 것 같음
    return answer