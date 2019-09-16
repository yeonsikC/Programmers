def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_point = 0
    b_point = 0
    c_point = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            a_point += 1
        if answers[i] == b[i%8]:
            b_point += 1
        if answers[i] == c[i%10]:
            c_point += 1
            
    total_point = [a_point, b_point, c_point]
    for i in range(3):
        if total_point[i] == max(total_point):
            answer.append(i+1)
    return answer
