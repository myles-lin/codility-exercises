def solution(S):
    S = S.split()
    longestPassword = -1
    for word in S:
        if word.isalnum(): # if it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
            alpha, digit = 0, 0
            for i in word: 
                if i.isalpha(): alpha += 1
                elif i.isdigit(): digit += 1
            if alpha % 2 == 0 and digit % 2 == 1 and len(word) > longestPassword: # even number of letters and odd number of digits.
                longestPassword = len(word)
                
    return longestPassword

S = "test 5 a0A pass007 ?xy1"
solution(S)
