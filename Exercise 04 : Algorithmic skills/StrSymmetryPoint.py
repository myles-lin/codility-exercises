def solution(S):
    n = len(S)
    if n == 0 or n % 2 == 0:
        return -1
    elif S == S[::-1]:
        return n//2
    else:
        return -1
    
# S = 'car'# answer = -1
# S = 'racecar' # answer = 3
# S = 'x' # answer = 0
# solution(S)

# Analysis
# Detected time complexity: O(length(S))
