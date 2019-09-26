n = 913893014
def solution(n):
	# 1. int형 n을 str형으로 변환 후, reverse=True(내림차순)이라는 옵션을 사용하며 sorted함수를 사용한다.
    total = sorted(str(n), reverse=True)
	
	# 2. total에서 문자를 하나씩 가져오며 모두 합친다. 합친 뒤, int형으로 형변환.
    return int(''.join(i for i in total))
solution(n)