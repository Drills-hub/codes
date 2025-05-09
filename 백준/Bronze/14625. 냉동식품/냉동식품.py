start_hour, start_minute = map(int, input().split())
stop_hour, stop_minute = map(int, input().split())
N = input()

count_N = 0

while True:
    hour_str = str(start_hour).zfill(2)
    minute_str = str(start_minute).zfill(2)
    if N in hour_str or N in minute_str:
        count_N += 1

    if start_hour == stop_hour and start_minute == stop_minute:
        break

    start_minute += 1
    if start_minute == 60:
        start_hour += 1
        start_minute = 0
    if start_hour == 24:
        start_hour = 0

print(count_N)