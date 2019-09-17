def solution(a, b):
    answer = ''
    day = 0    
    
    # 1. 요일 리스트 작성(16년 1월 1일이 금요일이므로 금요일부터 시작)
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    # 2. 각 월별 일수 리스트 작성(16년 2월의 경우 윤달이므로 29일.)
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 3. 해당월 직전까지, 각 월별 일수를 더함.
    # ex) 3월 24일 : day = 1월 * 31일 + 2월 * 29일
    if a > 1:
        for i in range(a-1):
            day += month[i]
    
    # 4. 해당월 일자는 #3에서 구한값에 더함.
    # ex) day += 24일
    day += b
    
    # 5. day를 7로 나눈 나머지에 1을 빼고, 요일 리스트에서 인덱싱.
    answer = week[day%7-1]
    return answer