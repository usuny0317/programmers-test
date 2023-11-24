"""

입력 #1

string 5
출력 #1

stringstringstringstringstring

"""

a, b = input().strip().split(' ')
b = int(b)
c=""
for i in range(0,b):
    c=c+a

print(c)