from collections import defaultdict

def solution(A):
    val_cnt = defaultdict(int)
    result = -1
    for val in A:
        val_cnt[val] += 1
        
    ans = sorted(val_cnt, key=lambda x: val_cnt[x])

    if val_cnt[ans[0]] == 1:
        result = ans[0]
        
    return result

# Analysis
# Detected time complexity: O(N * log(N))

# test data as below,
# A = [4, 10, 5, 4, 2, 10] # answer = 5
# A = [1, 4, 3, 3, 1, 2] # answer = 4
# A = [6, 4, 4, 6] # answer = -1
# A = [1, 1, 1, 2, 3, 3, 3] # answer = 2
# solution(A)
