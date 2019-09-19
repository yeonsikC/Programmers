def solution(n):
    # 1. set을 이용하여 집합으로 만듬.
    num = set(range(2, n+1))
    
    # 2. 하나씩 돌면서 i가 num에 속한다면, 그 다음 i의 배수 값부터, num에서 제거한다.
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            
    return len(num)