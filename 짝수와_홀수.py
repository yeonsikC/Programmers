def solution(num):
	# 1. num이 짝수면 num%2 == 1 (= True), 홀수면 num%2 == 0 (=False)
	# 2. (True일 때의 값) if (조건식) else (False일 때의 값)
    return 'Even' if num%2 else 'Odd'