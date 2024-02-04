from datetime import datetime, timedelta

H, M = map(int, input().split())
C = int(input())

current_time = datetime(2022, 1, 2, H, M)

finish_time = current_time + timedelta(minutes=C)

print(finish_time.hour, finish_time.minute)
