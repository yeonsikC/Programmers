def solution(arr):
    answer = [arr[0]]
    
    # 1. 해당 인덱스값이 이전 인덱스값과 다를 경우만 answer에 추가.
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
