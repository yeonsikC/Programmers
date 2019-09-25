def solution(arr, divisor):
    answer = []
    # 1. arr 배열의 각 원소별로 divisor로 나누고, 만약 나머지가 0이라면 answer에 추가.
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
            
    # 2. 만약, answer에 하나도 추가되지 않았다면 -1 추가.
    if len(answer)==0:
        answer.append(-1)
        
    # 3. answer 정렬.
    answer = sorted(answer)
    return answer
