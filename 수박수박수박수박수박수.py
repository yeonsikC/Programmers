def solution(n):
    s = '수박'
    answer = ''
    if n%2 > 0:
        answer = s*(n//2)
        answer += s[0]
    else:
        answer = s*(n//2)
    return answer
	
'''
아래는 가장 짧은 코드입니다.
def solution(n):
	s = '수박' * n%2
	return s[:n]
'''