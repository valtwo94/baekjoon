import sys

# 첫 번째 줄에서 전체 테스트 케이스의 개수 T를 읽어옴
T = int(sys.stdin.readline())

# 각 테스트 케이스에 대한 처리
for _ in range(T):
    # A, B를 공백으로 구분하여 읽어옴
    A, B = map(int, sys.stdin.readline().split())

    # 여기서 각 테스트 케이스에 대한 작업을 수행
    print(A + B)