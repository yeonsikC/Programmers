def solution(s):
    answer = True
    chk = 0
  
    # 1. 각 알파벳을 비교하여 p면 +1, y면 -1을 chk에 더함.
    for str in s:
        if str == 'p' or str == 'P':
            chk += 1
        elif str == 'y' or str == 'Y':
            chk -= 1
    
    # 2. 최종적으로 chk 값이 0이면 True 아니면 False
    if chk != 0:
        answer = False
    

    return answer

'''
# 아래는 간결한 코드입니다.

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
'''
