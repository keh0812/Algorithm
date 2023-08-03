def solution(n, k):
    answer = 0
    
    service = int(n/10)
    dish = n*12000
    drink = (k-service)*2000
        
    return dish + drink