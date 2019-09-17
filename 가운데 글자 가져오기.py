def solution(s):
    answer = ''
    
    # 1. 만약, 단어 s의 길이가 홀수라면
    if len(s)%2 == 1:
        answer = s[len(s)//2]
    
    # 2. 짝수라면
    else:
        answer = s[len(s)//2-1:len(s)//2+1]
        
    return answer