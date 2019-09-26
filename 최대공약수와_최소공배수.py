n, m = 13, 16
def solution(n, m):
    a = n
    div = []
    if m%n != 0:
        for i in range(1, n):
            if n%(n-i) == 0:
                div.append(n-i)
        div = sorted(div, reverse = True)
        for i in range(len(div)):
            if m % div[i] == 0:
                a = div[i]
                break
        
    b = m
    i = 1
    while b < b*m:
        i += 1
        if b%n == 0:
            break
        else :
            b = m * i
    return [a, b]
solution(n, m)

'''
좋은 코드

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
'''