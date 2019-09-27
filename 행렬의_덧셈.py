def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[0])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
    return answer
	
'''
아래는 한줄코드
def solution(arr1,arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    return answer
'''