"""
문제 설명
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	queries	result
"rermgorpsam"	[[2, 3], [0, 7], [5, 9], [6, 10]]	"programmers"
"""
def solution(my_string, queries):
    answer = ''
    a=[]
    for i in my_string:
        a.append(i)
    for i in queries:
        j=0
        for k in range(i[0],i[1]+1,1):
            if i[1]-j<k:
                continue
            temp=a[k]
            a[k]=a[i[1]-j]
            a[i[1]-j]=temp
            j=j+1
    for i in a:
        answer=answer+str(i)
    return answer