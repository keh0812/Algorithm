def solution(s):
    answer = []
    a = s.split(' ')
    for i in range(len(a)) :
        if a[i].isalpha() == True :
            answer.append(a[i].capitalize())
        elif a[i].isalnum() == True :
            answer.append(a[i].lower())
        else :
            answer.append(a[i])
    return ' '.join(map(str, answer))