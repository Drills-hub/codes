def solution(phone_number):
    hid= '*' * (len(phone_number)-4)
    answer = hid + phone_number[-4:] 
    return answer