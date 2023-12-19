"""
문제 설명
정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스
위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을
return 하는 solution 함수를 작성해 주세요.

입출력 예
arr	n	result
[49, 12, 100, 276, 33]	27	[76, 12, 127, 276, 60]
[444, 555, 666, 777]	100	[444, 655, 666, 877]
"""
def solution(arr, n):
    answer = []
    if len(arr)%2==0: #짝수
        for i in range(0,len(arr),1):
            if i%2!=0:
                answer.append(n+arr[i])
            else:
                answer.append(arr[i])
    else: #홀수
        for i in range(0,len(arr),1):
            if i%2==0:
                answer.append(n+arr[i])
            else:
                answer.append(arr[i])
    return answer