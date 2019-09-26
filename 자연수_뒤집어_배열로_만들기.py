n=31425
def solution(n):
    sum = []
    for i in str(n):
        sum.insert(0,i)
    return sum
solution(n)

'''
가장 간단한 풀이식
def solution(n):
    return list(map(int, reversed(str(n))))
'''