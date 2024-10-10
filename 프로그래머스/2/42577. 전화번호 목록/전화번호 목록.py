def solution(phone_book):
    answer = True
    mydict = {}
    for i in phone_book:
        ans = ''
        for j in i:
            ans = ans + j
            if mydict.get(ans):
                mydict[ans]= mydict[ans] + 1
            else:
                mydict[ans]=1
    for i in phone_book:
        if mydict.get(i) > 1:
            answer= False
            break   
    return answer