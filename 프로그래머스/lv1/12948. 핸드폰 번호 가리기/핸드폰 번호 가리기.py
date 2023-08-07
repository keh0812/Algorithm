def solution(phone_number):
    chg = phone_number[:-4]
    return phone_number.replace(chg,len(chg)*"*")