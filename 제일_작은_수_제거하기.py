arr = [5, 1, 2, 100, 38, 83, 9, 84, 3]

def solution(arr):

	# 1. arr배열의 길이가 1이면, 값을 하나 뺀 뒤 return할 배열이 없으므로 -1 return
    if len(arr) == 1:
        return [-1]
    else:
		
		# 2. arr 배열에서 가장 작은값이 있는 index를 구한 뒤, 배열에서 제거
        arr.pop(arr.index(min(arr)))
        return arr

solution(arr)