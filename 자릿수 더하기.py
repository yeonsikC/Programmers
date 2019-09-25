def solution(n):
	# 1. n을 문자열로 바꾸고, 첫번째 인덱스부터 차례로 호출, 호출된 값을 정수형으로 변환한 후 sum.
    return  sum(int(s) for s in str(n))