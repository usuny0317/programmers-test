"""
입출력 예
ineq	eq	n	m	result
"<"	"="	20	50	1
">"	"!"	41	78	0
"""
def solution(ineq, eq, n, m):
    answer = 0
    if eq=="=":
        if ineq=="<":
            if n<=m: answer=1
        else:
            if n>=m: answer=1
    else:
        if ineq=="<":
            if n<m: answer=1
        else:
            if n>m: answer=1
    return answer