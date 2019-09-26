def solution(num):
    cnt = 0
    while num > 1:
        if num%2:
            num = num*3 + 1
        else:
            num = num/2
        cnt += 1
        if cnt == 500:
            cnt = -1
            break
    return cnt