n = 121

# 1. 제곱근을 위한 numpy 호출 ( n = n**(1/2)로 대체 가능)
import numpy as np
def solution(n):
	# 2. n의 제곱근을 int로 강제형변환 시킨 n의 제곱근으로 나눈 나머지가 0이라면.
    if np.sqrt(n)%int(np.sqrt(n)) == 0:
	
		# 3. 제곱근n에 1을 더한 값의 제곱을 리턴.
        return (int(np.sqrt(n))+1)**2
    else:
        return -1
		
solution(n)