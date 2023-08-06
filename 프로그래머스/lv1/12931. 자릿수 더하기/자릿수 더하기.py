def solution(n):
    num = str(n)
    answer = 0
    for i in list(num) :
        answer += int(i)
    return answer