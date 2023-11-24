"""입력 #1
4 5
출력 #1
4 + 5 = 9"""

a, b = map(int, input().strip().split(' '))
print("%d + %d = %d" % (a,b, a+b))