import numpy as np
def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
	    
		# 1. 슬라이싱
        step1 = array[commands[i][0]-1:commands[i][1]]
		
		# 2. 정렬
        step2 = np.sort(step1)
		
		# 3. 지정한 인덱스 값 추출
        step3 = step2[commands[i][2]-1]
		
		# 4. 하나씩 answer에 담기.
        answer.append(step3)
    
    return answer
