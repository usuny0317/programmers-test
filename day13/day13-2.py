"""
문제 설명
정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로
나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

입출력 예
num_list	n	result
[2, 1, 6]	1	[1, 6, 2]
[5, 2, 1, 7, 5]	3	[7, 5, 5, 2, 1]
"""
def solution(num_list, n):
    a=num_list[n:]
    b=num_list[:n]
    return a+b