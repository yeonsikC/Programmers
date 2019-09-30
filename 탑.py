def solution(heights):
    answer = []
    for i in range(1, len(heights)+1):
        j = i
        while j < len(heights):
            if heights[-i] < heights[-(j+1)]:
                answer.insert(0, len(heights)-j)
                break
            elif j == len(heights)-1:
                answer.insert(0, 0)
                break
            j += 1
    answer.insert(0, 0)
    return answer