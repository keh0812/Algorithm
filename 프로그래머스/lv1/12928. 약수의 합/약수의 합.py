def solution(n): 
    num = []
    for i in range(n) :
        i += 1
        if n%i == 0 :
            num.append(i)
    return sum(num)