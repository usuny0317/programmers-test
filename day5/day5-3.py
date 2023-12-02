"""
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

입출력 예
a	b	c	result
2	6	1	9
5	3	3	473
4	4	4	110592
"""

def solution(a, b, c):
    answer = 0
    if a==b:
        if b==c:#다 같을 때
            answer=(a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c)
        elif b!=c and a!=c:#ab 같고 bc ac 다를  떄
            answer=(a+b+c)*(a*a+b*b+c*c)
    elif b!=c and a!=c: #다 다를 때
        answer=a+b+c
    elif b==c: #ab다르고 bc 같을 때
        answer=(a+b+c)*(a*a+b*b+c*c)
    elif a==c: #ab다르고 ac 같을 때
        answer=(a+b+c)*(a*a+b*b+c*c)
    return answer