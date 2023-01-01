from math import ceil
def solution(E, L):
    E1, E2 = [int(i) for i in E.split(":")]
    L1, L2 = [int(i) for i in L.split(":")]
    E_minutes = E1 * 60 + E2
    L_minutes = L1 * 60 + L2
    time = L_minutes - E_minutes
        
    return 2 + 3 + 4 * ceil((time-60) / 60)

# E = "10:00" # answer = 17
# L = "13:21"
# E = "09:42" # answer = 9
# L = "11:42"
# solution(E, L)
