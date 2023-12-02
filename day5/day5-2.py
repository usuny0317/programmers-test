"""
입출력 예 #1

예제 1번은 a와 d가 각각 3, 4이고 included의 길이가 5입니다. 이를 표로 나타내면 다음과 같습니다.

1항	2항	3항	4항	5항
등차수열	3	7	11	15	19
included	true	false	false	true	true
따라서 true에 해당하는 1항, 4항, 5항을 더한 3 + 15 + 19 = 37을 return 합니다.

입출력 예 #2

예제 2번은 a와 d가 각각 7, 1이고 included의 길이가 7입니다. 이를 표로 나타내면 다음과 같습니다.

1항	2항	3항	4항	5항	6항	7항
등차수열	7	8	9	10	11	12	13
included	false	false	false	true	false	false	false
따라서 4항만 true이므로 10을 return 합니다.
"""
def solution(a, d, included):
    answer = 0
    now=a
    for i in range(0, len(included),1):
        if included[i]:
            answer=answer+now
        now=now+d
    return answer