import collections

def solution(participant, completion):
    
    # 1. collections 모듈에서 Counter라는 객체를 이용하여 두 리스트의 차를 구한다.
    last_one = collections.Counter(participant) - collections.Counter(completion)
    
    # 2. 하나 남은 차의 key 값을 가져온다.
    answer = list(last_one.keys())[0]
    
    return answer