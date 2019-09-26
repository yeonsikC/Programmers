def solution(x):
	# 1. x를 str로 형변환 후, 한글자(숫자)씩 가져와서 int형으로 형변환. 모든 숫자를 더한 값으로 x를 나누었을 때, 나머지가 0이라면 True, 아니면 False
    return False if x % sum(int(i) for i in str(x)) else True