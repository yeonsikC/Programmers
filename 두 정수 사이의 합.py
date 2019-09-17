def solution(a, b):
    answer = 0
	
	# 1. a와 b 중, 작은 값 이상 ~ 큰 값 이하만큼 원소 덧셈.
    for i in range(min(a,b), max(a,b)+1):
        answer += i
    return answer