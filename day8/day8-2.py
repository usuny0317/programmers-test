"""
문제 설명
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

입출력 예
a	b	c	d	result
2	2	2	2	2222
4	1	4	4	1681
6	3	3	6	27
2	5	2	6	30
6	4	2	5	2

"""

def solution(a, b, c, d):
    answer = 0
    if a == b == c == d:  # 모두 같은 경우
        answer = 1111 * a
    elif a != b and b == c == d:  # a다르고 다 같은 경우
        answer = (10 * b + a) ** 2
    elif b != a and a == c == d:  # b 다르고 다 같은 경우
        answer = (10 * a + b) ** 2
    elif c != a and a == b == d:  # c다르고 다 같은 경우
        answer = (10 * a + c) ** 2
    elif d != a and a == b == c:  # d다르고 다 같은 경우
        answer = (10 * a + d) ** 2
    elif a == b and a != c and c == d:  # ab 같고 cd 같은 경우
        answer = (a + c) * abs(a - c)
    elif a == c and a != b and b == d:  # ac bd
        answer = (a + b) * abs(a - b)
    elif a == d and a != b and b == c:  # ad bc
        answer = (a + b) * abs(a - b)
    elif a == b and a != c and a != d and c != d:  # ab c d
        answer = c * d
    elif a == c and a != b and a != d and b != d:  # ac b d
        answer = b * d
    elif a == d and a != b and a != c and b != c:  # ad b c
        answer = b * c
    elif b == c and b != a and b != d and a != d:  # bc a d
        answer = a * d
    elif b == d and b != a and b != c and a != c:  # bd a c
        answer = a * c
    elif c == d and c != a and c != b and a != b:  # cd a b
        answer = a * b
    else:
        answer = min(a, b, c, d)

    return answer

# 다른 사람 풀이
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)


#다른 사람 풀이
def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)