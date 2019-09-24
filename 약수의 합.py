def solution(n):
	# 1. 1부터 n까지 돌면서, n을 그 값으로 나누었을 때 나머지가 0인 경우만 더한다.
    return sum([i for i in range(1, n+1) if n%i == 0 ])