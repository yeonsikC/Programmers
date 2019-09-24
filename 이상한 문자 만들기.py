def solution(s):
    answer = ''
	
	# 1. 문자열 s를 공백으로 분리한 후, 각 단어별로 반복
    for i in s.split(' '):
		
		# 2. 각 단어별 알파벳별로 반복
        for j in range(len(i)):
		
			# 3. 단어별 인덱스가 짝수의 경우 대문자.
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
				
		# 4. 단어 하나가 끝날 때마다 한칸 띄어쓰기.
        answer += ' '
		
	# 5. 마지막 단어가 끝나고나서도 띄어쓰기가 적용되므로 return값에서 마지막 띄어쓰기를 빼준다.
    return answer[:-1]