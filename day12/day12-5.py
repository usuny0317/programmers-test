"""
문제 설명
정수 배열 arr와 query가 주어집니다.
query를 순회하면서 다음 작업을 반복합니다.
짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.

입출력 예
arr	query	result
[0, 1, 2, 3, 4, 5]	[4, 1, 2]	[1, 2, 3]
"""
def solution(arr, query):
    for i in range(0,len(query),1):
        if i%2==0:
            arr=arr[:query[i]+1]
        elif i%2!=0:
            arr=arr[query[i]:]
    return arr

#query 값 아님...
#query[i]에서 i 값의 홀짝임... 그니까 4는 0번 인덱스로 0이니까 짝수... 1은 1번 인덱스니 1이니까 홀수... 2는 3번 인덱스니...3이니까 홀수.. 염병...