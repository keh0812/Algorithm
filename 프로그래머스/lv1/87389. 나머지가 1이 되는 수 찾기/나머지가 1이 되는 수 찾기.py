def solution(n):
    answer = 0
    
    for i in range(n) :
        i = i + 1
        if n%i == 1 :
            answer = i
            break
    return answer