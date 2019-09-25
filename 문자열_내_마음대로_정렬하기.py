def solution(strings, n):
    answer = []
    
    # 1. 각 단어 앞에 n번째 알파벳을 붙힌다.
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    
    # 2. 맨 앞글자 단어로 sort 실시.
    strings = sorted(strings)
    
    # 3. answer에는 맨 앞글자를 제외하여 추가한다.
    for i in range(len(strings)):
        answer.append(strings[i][1:])
        
    return answer
