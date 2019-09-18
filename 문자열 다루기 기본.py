def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        try:
            _ = int(s)
            answer = True
        except Exception:
            answer = False
    return answer