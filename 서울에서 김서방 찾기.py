def solution(seoul):
    # 1. 각 인덱스를 'Kim'과 비교.
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = "김서방은 "+str(i)+"에 있다"
            break
    return answer

'''
다음은 index 함수를 이용한 간단하고 효율적인 코드입니다.
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))
'''