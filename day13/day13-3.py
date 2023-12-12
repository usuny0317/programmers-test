"""
문제 설명
문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. "l"이나 "r"이 없다면 빈 리스트를 return합니다.

입출력 예
str_list	result
["u", "u", "l", "r"]	["u", "u"]
["l"]	[]
"""
def solution(str_list):
    answer = []
    for i in range(0, len(str_list),1):
        if str_list[i]=="l":
            answer=str_list[:i]
            break
        elif str_list[i]=="r":
            answer=str_list[i+1:]
            break
    return answer