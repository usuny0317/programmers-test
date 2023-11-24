"""입출력 예
my_string	overwrite_string	s	result
"He11oWor1d"	"lloWorl"	2	"HelloWorld"
"Program29b8UYP"	"merS123"	7	"ProgrammerS123" """

def solution(my_string, overwrite_string, s):
    a=my_string[:s]
    c=s+len(overwrite_string)
    b=my_string[c:]
    answer = a+overwrite_string+b
    return answer