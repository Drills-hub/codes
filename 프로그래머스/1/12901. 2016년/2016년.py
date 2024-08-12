 #datetime 모듈사용
import datetime

def solution(a, b):
    #weekday()에 맞춰 월요일을 0번 인덱스에 정렬
    week=['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    day = datetime.date(2016, a, b)
    week_day = day.weekday()
    
    return ''.join(week[week_day])