def solution(s):
    answer = ''
    
    # 1. 문자열 s의 길이가 0이 될 때 까지 반복.
    while len(s) > 0:
        
        # 1. 첫 알파벳이 전체 문장 중, 가장 큰값이랑 비교하며 answer에 추가.
        if s[0] == max(s):
            answer += s[0]
            s = s[1:]
            
        # 2. 만약 첫 알파벳이 큰 값이 아닐 경우, 문자열의 맨 마지막으로 이동.
        else:
            s += s[0]
            s = s[1:]
    return answer