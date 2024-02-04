from datetime import datetime, timedelta

H, M = map(int, input().split())

current_time = datetime(2022, 1, 1, H, M)

new_time = current_time - timedelta(minutes=45)

new_H = new_time.hour

new_M = new_time.minute

print(new_H, new_M)