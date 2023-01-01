def solution(N):
    count = 0
    while N % 2 == 0:
        N /= 2
        count += 1
    
    return count

# N = 24 # answer = 3
# solution(N)
