"""
문제 설명
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수,
my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수,
my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의
정수 배열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	result
"Programmers"
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3,
1, 0, 0, 0, 0, 0, 0, 0]
"""

def solution(my_string):
    answer = []
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M'
           ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            "a","b","c","d","e","f","g","h","i","j","k","l","m"
           ,"n","o","p","q",'r','s','t','u','v','w','x','y','z']
    cou=[0 for i in range(0,len(alpha),1)]
    for i in my_string:
        if i in alpha:
            a=alpha.index(i)
            cou[a]=cou[a]+1
    answer=cou
    return answer